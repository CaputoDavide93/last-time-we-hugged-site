# 🛠️ Troubleshooting

## A page returns 404 on GitHub Pages

Pages serves the `main` branch root. Check that the folder holds an
`index.html` and that the link ends with a slash (`/privacy/`). A merge can take
a minute to publish.

## `make check` reports "missing page"

One of `index.html`, `privacy/index.html` or `contact/index.html` is gone.
Restore it from git history.

## `make check` reports "canonical is ..."

A page's `<link rel="canonical">` does not match its published address. Use the
address with a trailing slash, for example `.../privacy/`.

## `make check` reports "broken link"

A relative link or image path does not resolve from that page. Pages one folder
deep use `../`.

## `make check` reports "unexpected address"

A `mailto:` link names an address other than the support address. Use the
address already on the contact page.

## `make check` reports "stale diagrams"

Run `make diagram` and commit the SVGs.

## `make screenshots` fails

It needs network access once to install Playwright and download Chromium. Run
`make screenshots` again, or delete `.venv-screenshots/` to start clean.

## The page looks unstyled when opened as a file

The links use relative paths and work from a file, but a browser may block some
behaviour from `file://`. Use `make serve` and open <http://localhost:8000/>.
