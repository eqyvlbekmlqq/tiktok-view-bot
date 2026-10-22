"""Session pool — reuses simulated viewer sessions across dispatches."""
from __future__ import annotations

import json
import uuid
from pathlib import Path

from loguru import logger


class SessionManager:
    def __init__(self, session_dir: Path, max_per_session: int = 5) -> None:
        self.session_dir = session_dir
        self.max_per_session = max_per_session
        self.session_dir.mkdir(parents=True, exist_ok=True)
        self._active: dict[str, dict] = {}

    def acquire(self, proxy: str) -> dict:
        sid = str(uuid.uuid4())
        session = {
            "sid": sid,
            "proxy": proxy,
            "views": 0,
            "device_id": uuid.uuid4().hex,
        }
        self._active[sid] = session
        return session

    def release(self, session: dict) -> None:
        sid = session["sid"]
        if sid in self._active:
            del self._active[sid]

    def persist(self, session: dict) -> Path:
        path = self.session_dir / f"{session['sid']}.json"
        path.write_text(json.dumps(session, indent=2))
        logger.debug("persisted session {}", session["sid"])
        return path