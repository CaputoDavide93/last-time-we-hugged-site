# One entry point for the checks CI runs. `make check` before every push.

.PHONY: check diagram screenshots social serve

check: ## Everything CI checks
	python3 tools/check_site.py
	python3 tools/gen_diagram.py --check

diagram: ## Redraw docs/assets/architecture-*.svg
	python3 tools/gen_diagram.py

serve: ## Preview the site at http://localhost:8000
	python3 -m http.server 8000

screenshots: ## Retake docs/assets/screenshots/ from the served site (not CI)
	test -x .venv-screenshots/bin/python || ( \
		python3 -m venv .venv-screenshots && \
		.venv-screenshots/bin/pip install -q -r tools/screenshots/requirements.txt )
	.venv-screenshots/bin/python -m playwright install chromium
	.venv-screenshots/bin/python tools/screenshots/take_screenshots.py

social: ## Redraw docs/assets/brand/icon.png and social-preview.png (not CI)
	.venv-screenshots/bin/python tools/screenshots/social_preview.py
