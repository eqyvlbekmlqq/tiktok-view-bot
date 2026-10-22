"""Centralized loguru setup for the viewer bot."""
from __future__ import annotations

import sys
from pathlib import Path
from loguru import logger


def setup_logger(level: str = "INFO", log_dir: Path | None = None) -> None:
    logger.remove()
    logger.add(sys.stderr, level=level, format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | {message}")
    if log_dir:
        log_dir.mkdir(parents=True, exist_ok=True)
        logger.add(log_dir / "viewer.log", rotation="5 MB", retention=3, level=level)