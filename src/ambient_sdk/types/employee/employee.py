# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..employee_core import EmployeeCore

__all__ = ["Employee"]


class Employee(EmployeeCore):
    id: Optional[str] = None
    """Unique identifier for the employee."""

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)
    """When the employee was archived."""

    archived_reason: Optional[str] = FieldInfo(alias="archivedReason", default=None)
    """Reason for archiving the employee record."""

    balance: Optional[float] = None
    """The balance of the account."""

    bank_account_no: Optional[str] = FieldInfo(alias="bankAccountNo", default=None)
    """The bank account number of the employee in passport."""

    bank_routing_no: Optional[str] = FieldInfo(alias="bankRoutingNo", default=None)
    """The bank routing number of the employee in passport."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the employee record was created."""

    debit_id: Optional[str] = FieldInfo(alias="debitId", default=None)
    """Unique identifier for the debit card."""

    passport_account_id: Optional[str] = FieldInfo(alias="passportAccountId", default=None)
    """Account ID for passport processing."""

    passport_customer_id: Optional[str] = FieldInfo(alias="passportCustomerId", default=None)
    """Customer ID for passport processing."""
