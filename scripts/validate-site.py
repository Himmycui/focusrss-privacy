#!/usr/bin/env python3
"""Validate the dependency-free FocusRSS public legal and support site."""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
LEGAL_INPUTS = ROOT / "docs/legal/LEGAL_INPUTS.yaml"

REQUIRED_ROUTES = (
    "/",
    "/privacy/",
    "/terms/",
    "/support/",
    "/privacy-choices/",
    "/en/",
    "/en/privacy/",
    "/en/terms/",
    "/en/support/",
    "/en/privacy-choices/",
)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hrefs: list[str] = []
        self.ids: set[str] = set()
        self.lang: str | None = None
        self.main_count = 0
        self.h1_count = 0
        self.title_count = 0
        self.script_count = 0
        self.form_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html":
            self.lang = values.get("lang")
        if tag == "a" and values.get("href"):
            self.hrefs.append(values["href"] or "")
        if tag == "link" and values.get("href"):
            self.hrefs.append(values["href"] or "")
        if values.get("id"):
            self.ids.add(values["id"] or "")
        if tag == "main":
            self.main_count += 1
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "title":
            self.title_count += 1
        elif tag == "script":
            self.script_count += 1
        elif tag == "form":
            self.form_count += 1


def route_file(route: str) -> Path:
    return SITE / route.lstrip("/") / "index.html"


def destination_file(source: Path, href: str) -> tuple[Path, str]:
    parsed = urlsplit(href)
    fragment = unquote(parsed.fragment)
    path = unquote(parsed.path)

    if path.startswith("/"):
        relative = PurePosixPath(path.lstrip("/"))
        target = SITE.joinpath(*relative.parts)
    elif path:
        target = source.parent / path
    else:
        target = source

    if path.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target.resolve(), fragment


def parse_page(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def yaml_scalar(key: str) -> str | None:
    text = LEGAL_INPUTS.read_text(encoding="utf-8")
    match = re.search(rf"^\s*{re.escape(key)}:\s*(?:\"([^\"]*)\"|([^#\n]+))", text, re.MULTILINE)
    if not match:
        return None
    return (match.group(1) or match.group(2) or "").strip()


def validate(allow_blocking_todos: bool) -> list[str]:
    errors: list[str] = []

    for route in REQUIRED_ROUTES:
        path = route_file(route)
        if not path.is_file():
            errors.append(f"required URL is missing: {route} ({path.relative_to(ROOT)})")

    marker_pattern = re.compile(r"TODO_BLOCKING|待填写", re.IGNORECASE)
    marker_files = [*sorted((ROOT / "docs/legal").rglob("*")), *sorted(SITE.rglob("*"))]
    if not allow_blocking_todos:
        for path in marker_files:
            if path.is_file() and marker_pattern.search(path.read_text(encoding="utf-8")):
                errors.append(f"unresolved build-blocking marker: {path.relative_to(ROOT)}")

    email = yaml_scalar("support_email")
    if not email:
        errors.append("support_email is absent from LEGAL_INPUTS.yaml")
    else:
        for route in ("/support/", "/en/support/"):
            path = route_file(route)
            if path.is_file() and email not in path.read_text(encoding="utf-8"):
                errors.append(f"support contact is absent from {route}")

    pages = sorted(SITE.rglob("*.html"))
    page_parsers: dict[Path, PageParser] = {}
    for page in pages:
        parser = parse_page(page)
        page_parsers[page.resolve()] = parser
        label = page.relative_to(ROOT)
        if not parser.lang:
            errors.append(f"missing html lang attribute: {label}")
        if parser.main_count != 1:
            errors.append(f"expected exactly one main element in {label}; found {parser.main_count}")
        if parser.h1_count != 1:
            errors.append(f"expected exactly one h1 in {label}; found {parser.h1_count}")
        if parser.title_count != 1:
            errors.append(f"expected exactly one title in {label}; found {parser.title_count}")
        if parser.script_count:
            errors.append(f"JavaScript is not allowed: {label}")
        if parser.form_count:
            errors.append(f"forms are not allowed on this static site: {label}")

        source_text = page.read_text(encoding="utf-8").lower()
        forbidden = ("google-analytics", "googletagmanager", "facebook.net", "doubleclick", "document.cookie")
        for token in forbidden:
            if token in source_text:
                errors.append(f"tracking or cookie token {token!r} found in {label}")

    for page, parser in page_parsers.items():
        for href in parser.hrefs:
            parsed = urlsplit(href)
            if parsed.scheme in {"mailto", "tel"}:
                continue
            if parsed.scheme or parsed.netloc or href.startswith("//"):
                errors.append(f"external asset/link is not allowed: {page.relative_to(ROOT)} -> {href}")
                continue
            target, fragment = destination_file(page, href)
            try:
                target.relative_to(SITE.resolve())
            except ValueError:
                errors.append(f"internal link escapes site root: {page.relative_to(ROOT)} -> {href}")
                continue
            if not target.is_file():
                errors.append(f"broken internal link: {page.relative_to(ROOT)} -> {href}")
                continue
            if fragment and target.suffix == ".html":
                target_parser = page_parsers.get(target) or parse_page(target)
                if fragment not in target_parser.ids:
                    errors.append(f"broken fragment: {page.relative_to(ROOT)} -> {href}")

    required_disclosures = {
        "/privacy/": ("90 天", "14 天", "iOS Keychain", "完整 RSS 订阅列表不会发送"),
        "/terms/": ("一次性购买", "自动续订", "Apple 标准", "可接受使用"),
        "/support/": ("himmy.cui@outlook.com", "恢复购买", "RSS", "AI 端点"),
        "/en/privacy/": ("90 days", "14 days", "iOS Keychain", "full RSS subscription list"),
        "/en/terms/": ("lifetime purchase", "auto-renewable", "Apple Standard", "Acceptable use"),
        "/en/support/": ("himmy.cui@outlook.com", "Restore Purchases", "RSS", "AI endpoint"),
    }
    for route, phrases in required_disclosures.items():
        path = route_file(route)
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"required disclosure {phrase!r} missing from {route}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--allow-blocking-todos",
        action="store_true",
        help="run structural checks while reporting publication blockers separately",
    )
    args = parser.parse_args()

    errors = validate(args.allow_blocking_todos)
    if errors:
        for error in errors:
            print(f"[site-validation] ERROR: {error}", file=sys.stderr)
        print(f"[site-validation] failed with {len(errors)} error(s)", file=sys.stderr)
        return 1

    suffix = " (blocking markers temporarily allowed)" if args.allow_blocking_todos else ""
    print(f"[site-validation] all checks passed{suffix}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
