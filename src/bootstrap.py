"""Entry point for the TikTok viewer bot.

Wires configuration, the viewer engine, and the CLI together.
"""
from __future__ import annotations

import asyncio
import click
from loguru import logger

from src.config.settings import load_settings
from src.core.viewer_engine import ViewerEngine
from src.services.proxy_pool import ProxyPool
from src.utils.logger import setup_logger


@click.command()
@click.option("--url", required=True, help="Target TikTok video URL")
@click.option("--views", default=100, show_default=True, help="Number of views to send")
@click.option("--concurrency", default=8, show_default=True, help="Parallel worker count")
@click.option("--dry-run", is_flag=True, help="Validate config without sending views")
def main(url: str, views: int, concurrency: int, dry_run: bool) -> None:
    settings = load_settings()
    setup_logger(settings.log_level)
    logger.info("tiktok-view-bot starting | target={} views={}", url, views)

    if dry_run:
        logger.warning("dry-run enabled, no views will be dispatched")
        return

    pool = ProxyPool.from_file(settings.proxy_file)
    engine = ViewerEngine(settings=settings, proxy_pool=pool, concurrency=concurrency)
    asyncio.run(engine.run(url=url, target_views=views))


if __name__ == "__main__":
    main()