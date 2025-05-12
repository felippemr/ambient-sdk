# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmployerRetrieveBankInfoResponse"]


class EmployerRetrieveBankInfoResponse(BaseModel):
    account_number: Optional[str] = FieldInfo(alias="accountNumber", default=None)
    """The employer's bank account number."""

    bank_name: Optional[str] = FieldInfo(alias="bankName", default=None)
    """The name of the employer's bank."""

    routing_number: Optional[str] = FieldInfo(alias="routingNumber", default=None)
    """The employer's bank routing number."""
