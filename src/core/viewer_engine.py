"""Viewer engine — orchestrates sessions, proxies, and view dispatch."""
from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from typing import Iterable

from loguru import logger
from tenacity import retry, stop_after_attempt, wait_exponential

from src.config.settings import Settings
from src.core.rate_limiter import RateLimiter
from src.core.session_manager import SessionManager
from src.handlers.view_dispatch import dispatch_view
from src.services.proxy_pool import ProxyPool


@dataclass
class ViewerEngine:
    settings: Settings
    proxy_pool: ProxyPool
    concurrency: int = 8
    _dispatched: int = field(default=0, init=False)

    async def run(self, url: str, target_views: int) -> int:
        sem = asyncio.Semaphore(self.concurrency)
        limiter = RateLimiter(self.settings.delay_min_ms, self.settings.delay_max_ms)
        session_mgr = SessionManager(self.settings.session_dir)

        async def worker(idx: int) -> bool:
            async with sem:
                await limiter.wait()
                proxy = self.proxy_pool.next()
                session = session_mgr.acquire(proxy)
                ok = await self._attempt_dispatch(url, session, proxy)
                session_mgr.release(session)
                return ok

        tasks = [worker(i) for i in range(target_views)]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        self._dispatched = sum(1 for r in results if r is True)
        logger.info("dispatch complete: {}/{} views accepted", self._dispatched, target_views)
        return self._dispatched

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=8))
    async def _attempt_dispatch(self, url: str, session, proxy) -> bool:
        return await dispatch_view(url=url, session=session, proxy=proxy, timeout=self.settings.request_timeout)