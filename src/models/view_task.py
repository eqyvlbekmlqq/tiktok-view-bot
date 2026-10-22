"""Data model for a single view dispatch task."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class TaskStatus(str, Enum):
    PENDING = "pending"
    DISPATCHED = "dispatched"
    FAILED = "failed"
    ACCEPTED = "accepted"


@dataclass
class ViewTask:
    video_url: str
    proxy: str | None = None
    status: TaskStatus = TaskStatus.PENDING
    attempts: int = 0
    created_at: datetime = field(default_factory=datetime.utcnow)
    error: str | None = None

    def mark(self, status: TaskStatus, error: str | None = None) -> None:
        self.status = status
        self.attempts += 1
        if error:
            self.error = error