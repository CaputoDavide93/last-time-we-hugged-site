#!/usr/bin/env python3
"""Retake docs/assets/screenshots/ from the site itself.

Serves the repository root on a local port, opens each page in Chromium in
light and dark mode, and saves PNGs with all metadata stripped. The site has no
user data, so every screenshot is the public page as published. The contact
page is left out on purpose: it shows the support address, and this repository
does not repeat it.

  make screenshots
"""
from __future__ import annotations

import functools
import http.server
import pathlib
import threading

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "docs" / "assets" / "screenshots"
SCREENS = {
    "home": ("/", 700),
    "privacy": ("/privacy/", 1100),
}
WIDTH = 900


def strip(path: pathlib.Path) -> None:
    """Re-save pixels only, so no text chunks or timestamps remain."""
    with Image.open(path) as im:
        clean = Image.new(im.mode, im.size)
        clean.putdata(list(im.getdata()))
        clean.save(path, optimize=True)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass

    handler = functools.partial(Quiet, directory=str(ROOT))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{server.server_address[1]}"
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for scheme in ("light", "dark"):
            ctx = browser.new_context(viewport={"width": WIDTH, "height": 1100},
                                      color_scheme=scheme, device_scale_factor=1)
            page = ctx.new_page()
            for name, (path, height) in SCREENS.items():
                page.set_viewport_size({"width": WIDTH, "height": height})
                page.goto(base + path)
                page.wait_for_load_state("networkidle")
                target = OUT / f"{name}-{scheme}.png"
                page.screenshot(path=str(target), full_page=False)
                strip(target)
                print("wrote", target.relative_to(ROOT))
            ctx.close()
        browser.close()
    server.shutdown()


if __name__ == "__main__":
    main()
