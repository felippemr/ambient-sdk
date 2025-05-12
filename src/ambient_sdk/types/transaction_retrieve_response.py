# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TransactionRetrieveResponse"]


class TransactionRetrieveResponse(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the transaction."""

    amount: Optional[float] = None
    """The amount of the transaction."""

    balance: Optional[float] = None
    """The balance of the account."""

    counterparty: Optional[str] = None
    """The counterparty's passport account number associated with the transaction."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time when the transaction was created."""

    ext_trans_id: Optional[str] = FieldInfo(alias="extTransId", default=None)
    """The external transaction ID the transaction."""

    message: Optional[str] = None
    """A message attached to the transaction."""

    passport_account_id: Optional[str] = FieldInfo(alias="passportAccountId", default=None)
    """The passport account number associated with the transaction."""

    processed_at: Optional[datetime] = FieldInfo(alias="processedAt", default=None)
    """The date and time when the transaction was processed."""

    type_text: Optional[str] = FieldInfo(alias="typeText", default=None)
    """The type of the transaction."""
