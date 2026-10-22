@echo off
REM Convenience launcher for tiktok-view-bot on Windows
setlocal
if not exist .venv (
    python -m venv .venv
    .venv\Scripts\pip install -r requirements.txt
)
.venv\Scripts\python -m src.bootstrap --url %1 --views %2
endlocal