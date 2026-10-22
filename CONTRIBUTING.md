# Contributing to tiktok-view-bot

Thanks for wanting to help improve the TikTok Viewer bot. This is a hobbyist /
educational project — please keep contributions focused on the viewer engine,
proxy rotation, session handling, and reporting layers.

## Ground rules

- Do **not** submit PRs that hardcode account credentials or proxy lists.
- Keep the viewer engine deterministic and testable where possible.
- Any new handler must register itself in `src/handlers/__init__.py`.
- Run `pytest tests/` before opening a PR.

## Local setup

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m src.bootstrap --dry-run
```

## Style

- Python 3.11+, type hints required on public functions.
- `ruff` and `mypy` run in CI — keep the diff clean.
- Log lines go through `utils.logger`, never `print()`.

## Reporting bugs

Open an issue with the bot version, the target video URL, and the relevant
`logs/viewer.log` excerpt. Redact proxies and session tokens.