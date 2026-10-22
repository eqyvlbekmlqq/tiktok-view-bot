"""Low-level view dispatch handler.

Sends the simulated playback request that TikTok counts as a view.
"""
from __future__ import annotations

import aiohttp
from fake_useragent import UserAgent
from loguru import logger

UA = UserAgent(browsers=["Chrome", "Safari"], platforms=["mobile"])


async def dispatch_view(url: str, session: dict, proxy: str, timeout: int = 15) -> bool:
    headers = {
        "User-Agent": UA.random,
        "Referer": "https://www.tiktok.com/",
        "Accept": "application/json, text/plain, */*",
    }
    connector = aiohttp.TCPConnector(ssl=False, limit=0)
    async with aiohttp.ClientSession(connector=connector, headers=headers) as client:
        try:
            async with client.get(
                "https://www.tiktok.com/api/view",
                params={"item_id": _extract_video_id(url)},
                proxy=f"http://{proxy}" if proxy else None,
                timeout=aiohttp.ClientTimeout(total=timeout),
            ) as resp:
                logger.debug("dispatch status={} proxy={}", resp.status, proxy)
                return resp.status == 200
        except aiohttp.ClientError as exc:
            logger.warning("dispatch failed: {}", exc)
            return False


def _extract_video_id(url: str) -> str:
    return url.rstrip("/").split("/")[-1].split("?")[0]