# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["HealthRetrieveStatusResponse"]


class HealthRetrieveStatusResponse(BaseModel):
    status: Optional[str] = None
    """The current health status of the service."""

    timestamp: Optional[datetime] = None
    """The date and time when the health check was performed."""
