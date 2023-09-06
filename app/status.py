"""Invite statuses."""

from enum import Enum, auto


class InviteStatus(Enum):
    """Invite processing status."""

    success = auto()
    unsuccessful = auto()
    failure = auto()
