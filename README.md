<div align="center">

<img src="docs/assets/brand/icon.png" width="96" alt="The Last Time We Hugged app icon: two small heads above a heart, one outline in black and one in bronze, on warm white">

# 🤍 Last Time We Hugged site

**Read what the Last Time We Hugged couples' journal keeps, and where, before you install it: privacy policy and support pages with no scripts, cookies or trackers**

![HTML](https://img.shields.io/badge/HTML-static-E34F26?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-light_and_dark-1572B6?logo=css3&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-hosted-222222?logo=github&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
[![CI](https://github.com/CaputoDavide93/last-time-we-hugged-site/actions/workflows/ci.yml/badge.svg)](https://github.com/CaputoDavide93/last-time-we-hugged-site/actions/workflows/ci.yml)

</div>

---

## ✨ Features

This repository is the public website for **Last Time We Hugged**, a private
journal for couples on iPhone, Apple Watch and Android. App stores need a
privacy policy and a support page, and the app opens both from its Settings.
This site is where they live. Open it at
[caputodavide93.github.io/last-time-we-hugged-site](https://caputodavide93.github.io/last-time-we-hugged-site/).

### Why it exists

An app where you write about arguments with your partner holds some of the most
personal text you own. Before you install it you want to know what it keeps,
who can read it and what leaves your phone. The answer has to sit on a page you
can read on that phone, without a cookie banner, and the stores want the same
page as a link.

So the policy is a plain static page. It says what stays on the phone, which
permissions are optional, what syncing sends and where, and how to delete
everything.

| | This site | A policy page on a generic site builder | A policy PDF |
|---|---|---|---|
| Scripts, cookies, analytics | None (a check fails the build if a script or form appears) | Often present | None |
| Readable on a phone | Yes, one column from 375 px | Depends on the theme | Pinch and zoom |
| Light and dark | Follows the reader's system setting | Depends on the theme | No |
| Stable URLs the stores can keep | `/privacy/` and `/contact/` | Tied to the builder | Tied to a file name |
| Review the change before it goes live | Pull request, then GitHub Pages publishes `main` | Edit in a web editor | Replace the file |

The trade-off: the pages are in English only, and GitHub Pages may keep
standard server logs for visitors. Both are stated on the site.

### Install in 3 steps

There is nothing to install to read the site. To preview or edit it you need
Python 3 and a browser.

1. **Clone:** `git clone https://github.com/CaputoDavide93/last-time-we-hugged-site.git && cd last-time-we-hugged-site`
2. **Serve:** `make serve` (the same as `python3 -m http.server 8000`).
3. **Open** <http://localhost:8000/>. Run `make check` before you push.

### What you get

| | Page | What it is |
|---|---|---|
| 🏠 | [Home](https://caputodavide93.github.io/last-time-we-hugged-site/) | What the app is, in a few lines |
| 🔒 | [Privacy policy](https://caputodavide93.github.io/last-time-we-hugged-site/privacy/) | What the app keeps and where, permissions, widgets and watch, syncing, backups, payments (none), sign-in, deleting your data, children. Linked from the app's Settings and the store listings |
| 💬 | [Contact](https://caputodavide93.github.io/last-time-we-hugged-site/contact/) | Support address and common questions. Linked from the app's Settings and the store listings |
| 🌗 | Light and dark | Follows the reader's system setting, in the app's own colours |
| 🚫 | No tracking | No scripts, forms, cookies or analytics, and a check that fails if one appears |
| 🔎 | Findable | Canonical URLs, a sitemap, `robots.txt` and `llms.txt` |
| 🧪 | Self-checking | `make check` verifies every page exists, every local link resolves, metadata is present and the support address is the only one |

---

## 📸 Screenshots

Taken from the served site by `make screenshots` (Chromium, 900 px wide). The
contact page is left out because it shows the support address.

<table>
<tr>
<td width="50%">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/screenshots/home-dark.png">
  <img src="docs/assets/screenshots/home-light.png" alt="The Last Time We Hugged home page: the headline 'Keep what you learn from an argument.' and a card of three short facts about the app">
</picture>
</td>
<td width="50%">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/screenshots/privacy-dark.png">
  <img src="docs/assets/screenshots/privacy-light.png" alt="The privacy policy page with an 'In short' card: no account, no servers, no analytics, nothing to buy, no AI">
</picture>
</td>
</tr>
</table>

---

## 🗺️ Architecture

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/architecture-dark.svg">
  <img src="docs/assets/architecture-light.svg" width="100%" alt="The app's Settings and the store listings link to this site; a reader's browser fetches static HTML and CSS from GitHub Pages.">
</picture>

How it is built is in [docs/how-it-works.md](docs/how-it-works.md).

---

## 🚀 Quick Start

```bash
make serve     # preview at http://localhost:8000
make check     # page, link, metadata and diagram checks, the same as CI
```

GitHub Pages publishes the `main` branch root, so a merged pull request is the
release. The privacy page must stay true to the app's own privacy document:
change the app first, then that document and this page together, with a new
effective date, before the store listings. More in [docs/setup.md](docs/setup.md).

---

## 🧪 Tested on

| Environment | Status |
|---|---|
| Chromium (Playwright 1.64.1) on macOS, light and dark | ✅ Screenshots and layout checked |
| `make check` on Python 3.12 (CI, Ubuntu) | ✅ Runs on every pull request |
| Safari and Firefox | ❔ Unverified: plain HTML and CSS, not tried here |
| Screen readers | ❔ Unverified |

---

## 📁 Repo structure

```text
last-time-we-hugged-site/
├── index.html             # 🏠 what the app is, three promises
├── privacy/index.html     # 🔒 privacy policy
├── contact/index.html     # 💬 contact and common questions
├── assets/                # 🎨 site.css, the app icon at four sizes (favicon, touch icon, header) and mark.svg
├── docs/                  # 📚 setup, how it works, FAQ, troubleshooting
│   └── assets/            # 🖼️ diagram, screenshots, brand icon, social preview
├── tools/                 # 🔧 check_site.py, gen_diagram.py, brand/, screenshots/
├── .github/workflows/     # 🤖 ci.yml runs make check
├── Makefile               # ⚙️ check, serve, diagram, screenshots, social
├── llms.txt               # 🤖 the site in one plain-text page for search tools
├── robots.txt  sitemap.xml  # 🔎 crawler files
├── AGENTS.md  CLAUDE.md   # 🧭 contributor notes
├── CONTRIBUTING.md  SECURITY.md  LICENSE
├── .nojekyll              # serve files as they are
└── .gitignore
```

---

## 🛠️ Troubleshooting

[docs/troubleshooting.md](docs/troubleshooting.md) lists symptoms and fixes:
a page that 404s on GitHub Pages, a failing `make check`. Common questions are
in [docs/faq.md](docs/faq.md). The full index is [docs/README.md](docs/README.md).

---

## 🔒 Security

See [SECURITY.md](SECURITY.md).

---

## 🤝 Contributing

Found a wrong sentence, a broken link or a page that reads badly on your
device? [Open an issue](https://github.com/CaputoDavide93/last-time-we-hugged-site/issues/new)
with the page address, your browser and operating system with versions, and a
screenshot if it is a layout problem. Reports from browsers and devices not
listed under Tested on are especially useful. Details are in
[CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📄 License

[MIT](LICENSE)

---

<p align="center"><sub>Made with ❤️ by <a href="https://github.com/CaputoDavide93">Davide Caputo</a></sub></p>
