# 🚀 Setup

You need Python 3 and a browser to preview and check the site. Screenshots
need `make screenshots`, which installs Playwright into `.venv-screenshots/`.

## 1. Clone and preview

```bash
git clone https://github.com/CaputoDavide93/last-time-we-hugged-site.git
cd last-time-we-hugged-site
make serve
```

Open <http://localhost:8000/>. The home page looks like this:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/screenshots/home-dark.png">
  <img src="assets/screenshots/home-light.png" width="480" alt="The Last Time We Hugged home page with the headline and three short facts">
</picture>

## 2. Edit a page

Every page is one `index.html` that links `assets/site.css`: the root for the
home page, `privacy/` and `contact/`. Do not change a page's folder name: the
app and the store listings link to it.

The privacy page must stay true to the app's own privacy document. If the
meaning of a statement changes, change the app's document first, then this
page, and update the "Effective" date.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/screenshots/privacy-dark.png">
  <img src="assets/screenshots/privacy-light.png" width="480" alt="The privacy policy page with its 'In short' card">
</picture>

## 3. Check

```bash
make check
```

It fails when a page is missing, a local link or image is broken, a page
contains a script, form or iframe, a page lacks a title, description or
canonical URL, the sitemap omits a page, or an address other than the support
address appears in a `mailto:` link.

## 4. Open a pull request

GitHub Pages serves the `main` branch root, so the merge is the release. Check
the live page afterwards at
`https://caputodavide93.github.io/last-time-we-hugged-site/`.

## Retake the images

```bash
make screenshots   # docs/assets/screenshots/
make social        # docs/assets/brand/icon.png and social-preview.png
make diagram       # docs/assets/architecture-{light,dark}.svg
```

The first two need network access once to install Playwright and download
Chromium. The contact page is never photographed: it shows the support address.
