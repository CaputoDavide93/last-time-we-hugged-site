#!/usr/bin/env python3
"""Structural checks for the static site. Exit 1 if any group fails.

  python3 tools/check_site.py

Checks: every page exists, every local link and asset resolves, no scripts,
forms or iframes, every page has a title, description and canonical URL, the
sitemap lists every page, and the only mailto address is the one the contact
page already carries.
"""
from __future__ import annotations

import pathlib
import re
import sys
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE = "https://caputodavide93.github.io/last-time-we-hugged-site/"
PAGES = ["", "privacy", "contact"]
ADDRESS = "caputodav@gmail.com"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.tags, self.meta, self.canonical = [], set(), {}, None
        self.title, self._in_title = "", False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.add(tag)
        if tag == "title":
            self._in_title = True
        for key in ("href", "src"):
            if key in a:
                self.links.append(a[key])
        if tag == "meta" and "name" in a:
            self.meta[a["name"]] = a.get("content", "")
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def page_path(page: str) -> pathlib.Path:
    return ROOT.joinpath(*([page] if page else []), "index.html")


def main() -> int:
    errors: list[str] = []
    for page in PAGES:
        path = page_path(page)
        if not path.exists():
            errors.append(f"missing page: {path.relative_to(ROOT)}")
            continue
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        p = Page()
        p.feed(text)
        if p.tags & {"script", "form", "iframe"}:
            errors.append(f"{rel}: script, form or iframe present")
        if not p.title.strip():
            errors.append(f"{rel}: no title")
        if not p.meta.get("description"):
            errors.append(f"{rel}: no meta description")
        want = BASE + (page + "/" if page else "")
        if p.canonical != want:
            errors.append(f"{rel}: canonical is {p.canonical}, expected {want}")
        for link in p.links:
            if re.match(r"^(https?:|mailto:|#)", link):
                continue
            target = (path.parent / link.split("#")[0]).resolve()
            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                errors.append(f"{rel}: broken link {link}")
        for addr in re.findall(r"mailto:([^?\"']+)", text):
            if addr != ADDRESS:
                errors.append(f"{rel}: unexpected address {addr}")
    sitemap = ROOT / "sitemap.xml"
    if sitemap.exists():
        listed = set(re.findall(r"<loc>([^<]+)</loc>", sitemap.read_text(encoding="utf-8")))
        for page in PAGES:
            url = BASE + (page + "/" if page else "")
            if url not in listed:
                errors.append(f"sitemap.xml: missing {url}")
    else:
        errors.append("missing file: sitemap.xml")
    for f in ("assets/site.css", "assets/mark.svg", "robots.txt", "llms.txt", ".nojekyll"):
        if not (ROOT / f).exists():
            errors.append(f"missing file: {f}")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"{len(PAGES)} pages OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
