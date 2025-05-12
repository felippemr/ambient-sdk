# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BalanceUpdateResponse"]


class BalanceUpdateResponse(BaseModel):
    id: Optional[str] = None

    message: Optional[str] = None

    new_balance: Optional[float] = FieldInfo(alias="newBalance", default=None)
    """The updated balance of the employee."""
