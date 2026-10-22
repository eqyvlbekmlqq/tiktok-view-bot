"""Simple randomized rate limiter to mimic human view cadence."""
from __future__ import annotations

import asyncio
import random


class RateLimiter:
    def __init__(self, min_ms: int, max_ms: int) -> None:
        self.min_s = min_ms / 1000
        self.max_s = max_ms / 1000
        self._lock = asyncio.Lock()

    async def wait(self) -> None:
        delay = random.uniform(self.min_s, self.max_s)
        async with self._lock:
            await asyncio.sleep(delay)