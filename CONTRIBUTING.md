# 🤝 Contributing

Fixes to wording, links and layout are welcome as a pull request or an issue.

## Report a problem

[Open an issue](https://github.com/CaputoDavide93/last-time-we-hugged-site/issues/new) with:

- the page address;
- your browser and operating system, with versions;
- what you saw and what you expected;
- a screenshot for a layout problem.

Reports from a browser or device that is not in the "Tested on" table of the
README are the most useful. Do not paste anything from your journal. A security
problem goes through a
[private advisory](https://github.com/CaputoDavide93/last-time-we-hugged-site/security/advisories/new)
instead, as [SECURITY.md](SECURITY.md) says.

## Change the site

1. Branch from `main`.
2. Edit the page. The privacy page must stay true to the app's own privacy
   document, so a change to the meaning of a statement goes through the app's
   repository first, then here with a new effective date.
3. Run `make check`. It must pass.
4. Open a pull request. GitHub Pages publishes `main` after the merge.

Rules: static HTML and CSS only (no scripts, forms, cookies, analytics or web
fonts), URLs never change, one support address and it stays out of the README,
docs and images.
