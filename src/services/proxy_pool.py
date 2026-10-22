"""Rotating proxy pool for the viewer bot."""
from __future__ import annotations

import itertools
from pathlib import Path

from loguru import logger


class ProxyPool:
    def __init__(self, proxies: list[str]) -> None:
        if not proxies:
            logger.warning("proxy pool is empty — running without proxies")
        self._proxies = proxies
        self._cycle = itertools.cycle(proxies) if proxies else None

    @classmethod
    def from_file(cls, path: Path) -> "ProxyPool":
        if not path.exists():
            logger.warning("proxy file {} missing, continuing without proxies", path)
            return cls([])
        lines = [ln.strip() for ln in path.read_text().splitlines() if ln.strip() and not ln.startswith("#")]
        return cls(lines)

    def next(self) -> str | None:
        return next(self._cycle) if self._cycle else None

    def __len__(self) -> int:
        return len(self._proxies)