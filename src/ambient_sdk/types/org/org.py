# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..org_core import OrgCore

__all__ = ["Org"]


class Org(OrgCore):
    id: Optional[int] = None
    """Unique identifier for the organization."""

    bank_account_no: Optional[str] = FieldInfo(alias="bankAccountNo", default=None)
    """The bank account number of the organzation in passport."""

    bank_routing_no: Optional[str] = FieldInfo(alias="bankRoutingNo", default=None)
    """The bank routing number of the organization in passport."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Date and time when the organization record was created."""

    passport_account_id: Optional[str] = FieldInfo(alias="passportAccountId", default=None)
    """Account ID for passport processing."""

    passport_customer_id: Optional[str] = FieldInfo(alias="passportCustomerId", default=None)
    """Customer ID for passport processing."""
