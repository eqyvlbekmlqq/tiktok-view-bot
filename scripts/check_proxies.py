"""Quick proxy health check used before running the viewer bot."""
from __future__ import annotations

import asyncio
import aiohttp
from pathlib import Path

PROXY_FILE = Path(__file__).resolve().parents[1] / "data" / "proxies.txt"


async def check(proxy: str, timeout: int = 8) -> bool:
    try:
        async with aiohttp.ClientSession() as s:
            async with s.get("https://api.ipify.org", proxy=f"http://{proxy}",
                             timeout=aiohttp.ClientTimeout(total=timeout)) as r:
                return r.status == 200
    except Exception:
        return False


async def main() -> None:
    proxies = [l.strip() for l in PROXY_FILE.read_text().splitlines() if l.strip() and not l.startswith("#")]
    results = await asyncio.gather(*(check(p) for p in proxies))
    for p, ok in zip(proxies, results):
        print(f"{'OK ' if ok else 'BAD'} {p}")


if __name__ == "__main__":
    asyncio.run(main())