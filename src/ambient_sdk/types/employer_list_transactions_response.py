# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmployerListTransactionsResponse", "EmployerListTransactionsResponseItem"]


class EmployerListTransactionsResponseItem(BaseModel):
    amount: Optional[float] = None
    """The amount of the transaction."""

    counterparty: Optional[str] = None
    """The counterparty's passport account number associated with the transaction."""

    date: Optional[datetime] = None
    """The date and time of the transaction."""

    passport_account_id: Optional[str] = FieldInfo(alias="passportAccountId", default=None)
    """The passport account number associated with the transaction."""

    transaction_id: Optional[str] = FieldInfo(alias="transactionId", default=None)
    """The unique identifier for the transaction."""

    type: Optional[str] = None
    """The type of transaction (e.g., "credit", "debit")."""


EmployerListTransactionsResponse: TypeAlias = List[EmployerListTransactionsResponseItem]
