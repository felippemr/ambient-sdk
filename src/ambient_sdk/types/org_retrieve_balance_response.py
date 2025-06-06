# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["OrgRetrieveBalanceResponse"]


class OrgRetrieveBalanceResponse(BaseModel):
    balance: Optional[float] = None
    """The current balance of the organization."""
