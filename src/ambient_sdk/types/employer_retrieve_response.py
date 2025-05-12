# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .employer_core import EmployerCore

__all__ = ["EmployerRetrieveResponse"]


class EmployerRetrieveResponse(EmployerCore):
    id: Optional[str] = None
    """Unique identifier for the employer record."""

    balance: Optional[float] = None
    """The balance of the account."""

    bank_account_no: Optional[str] = FieldInfo(alias="bankAccountNo", default=None)
    """The bank account number of the employer in passport."""

    bank_routing_no: Optional[str] = FieldInfo(alias="bankRoutingNo", default=None)
    """The bank routing number of the employer in passport."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Date and time when the employer record was created."""

    passport_account_id: Optional[str] = FieldInfo(alias="passportAccountId", default=None)
    """Account ID for passport processing."""

    passport_customer_id: Optional[str] = FieldInfo(alias="passportCustomerId", default=None)
    """Customer ID for passport processing."""
