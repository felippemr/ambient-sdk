# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OrgRetrieveBankInfoResponse"]


class OrgRetrieveBankInfoResponse(BaseModel):
    bank_account_no: Optional[str] = FieldInfo(alias="bankAccountNo", default=None)
    """The organization's bank account number."""

    bank_routing_no: Optional[str] = FieldInfo(alias="bankRoutingNo", default=None)
    """The organization's bank routing number."""
