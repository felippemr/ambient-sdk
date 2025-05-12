# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmployeeGetPaymentMethodsResponse"]


class EmployeeGetPaymentMethodsResponse(BaseModel):
    account_number: Optional[str] = FieldInfo(alias="accountNumber", default=None)
    """The employee's bank account number."""

    bank_name: Optional[str] = FieldInfo(alias="bankName", default=None)
    """The name of the employee's bank."""

    card_cvv: Optional[str] = FieldInfo(alias="cardCvv", default=None)
    """The employee's card CVV number."""

    card_expires: Optional[str] = FieldInfo(alias="cardExpires", default=None)
    """The employee's card expiration date in MM/YYYY format."""

    card_no: Optional[str] = FieldInfo(alias="cardNo", default=None)
    """The employee's card number."""

    routing_number: Optional[str] = FieldInfo(alias="routingNumber", default=None)
    """The employee's bank routing number."""
