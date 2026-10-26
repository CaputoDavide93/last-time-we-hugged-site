# 🧠 How it works

The site is plain files. There is no build step, no script and no framework.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/architecture-dark.svg">
  <img src="assets/architecture-light.svg" width="100%" alt="The app's Settings and the store listings link to this site; a reader's browser fetches static HTML and CSS from GitHub Pages.">
</picture>

## Pages and URLs

Three pages exist: home, `privacy/` and `contact/`. The app's Settings and the
store listings link to the privacy and contact pages, so these URLs do not
change, and neither does the repository name.

## Styles

`assets/site.css` holds the colours as variables, taken from the app's design
tokens. A `prefers-color-scheme: dark` block swaps them, so the page follows
the reader's system setting. The layout is one column up to 720 px. The mark
in `assets/mark.svg` is the favicon and the header logo.

## Search files

Each page carries a canonical URL and Open Graph tags (the preview image is
`docs/assets/social-preview.png`). `sitemap.xml` lists the three pages,
`robots.txt` allows all crawlers and points at the sitemap, and `llms.txt` is
the site in one plain-text page. There is no structured-data script, because
the site carries no scripts.

## Hosting

GitHub Pages serves the `main` branch root. `.nojekyll` makes it serve files as
they are. GitHub may keep standard server logs; the site says so in its footer
and in the privacy policy.

## Checks

`make check` runs `tools/check_site.py` (pages, links, metadata, sitemap, no
scripts, one address) and `tools/gen_diagram.py --check` (the diagram files
match the generator). CI runs the same command on every pull request.
