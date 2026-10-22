"""Optional account store for authenticated view sessions."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterator


class AccountStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self._accounts: list[dict] = []
        if path.exists():
            self._accounts = json.loads(path.read_text())

    def __iter__(self) -> Iterator[dict]:
        return iter(self._accounts)

    def add(self, username: str, cookie: str) -> None:
        self._accounts.append({"username": username, "cookie": cookie})
        self.path.write_text(json.dumps(self._accounts, indent=2))

    def count(self) -> int:
        return len(self._accounts)