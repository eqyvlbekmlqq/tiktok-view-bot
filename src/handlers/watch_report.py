"""Aggregates dispatch results into a human-readable report."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class WatchReport:
    target_url: str
    attempted: int
    accepted: int
    started_at: datetime
    finished_at: datetime

    @property
    def success_rate(self) -> float:
        return self.accepted / self.attempted if self.attempted else 0.0

    def render(self) -> str:
        return (
            f"TikTok Viewer bot report\n"
            f"  target:   {self.target_url}\n"
            f"  attempted: {self.attempted}\n"
            f"  accepted:  {self.accepted}\n"
            f"  success:   {self.success_rate:.1%}\n"
            f"  duration:  {(self.finished_at - self.started_at).total_seconds():.1f}s"
        )


def build_watch_report(url: str, attempted: int, accepted: int,
                       started_at: datetime, finished_at: datetime) -> WatchReport:
    return WatchReport(url, attempted, accepted, started_at, finished_at)