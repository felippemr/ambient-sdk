# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["PaymentMethodListResponse", "Employee"]


class Employee(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the employee."""

    account_number: Optional[str] = FieldInfo(alias="accountNumber", default=None)
    """The employee's bank account number."""

    bank_name: Optional[str] = FieldInfo(alias="bankName", default=None)
    """The name of the bank associated with the employee's account."""

    card_cvv: Optional[str] = FieldInfo(alias="cardCvv", default=None)
    """The employee's card CVV number."""

    card_expires: Optional[str] = FieldInfo(alias="cardExpires", default=None)
    """The employee's card expiration date in MM/YYYY format."""

    card_no: Optional[str] = FieldInfo(alias="cardNo", default=None)
    """The employee's card number."""

    debit_id: Optional[str] = FieldInfo(alias="debitId", default=None)
    """The employee's debit ID (This is not the card number)."""

    employee_id: Optional[str] = FieldInfo(alias="employeeId", default=None)
    """The employee's ID within the employer."""

    employer_id: Optional[str] = FieldInfo(alias="employerId", default=None)
    """The employer's ID within the organization."""

    org_id: Optional[int] = FieldInfo(alias="orgId", default=None)
    """The organization ID associated with the employee."""

    passport_account_id: Optional[str] = FieldInfo(alias="passportAccountId", default=None)
    """The passport account number associated with the employee."""

    passport_customer_id: Optional[str] = FieldInfo(alias="passportCustomerId", default=None)
    """The passport customer number associated with the employee."""

    routing_number: Optional[str] = FieldInfo(alias="routingNumber", default=None)
    """The employee's bank routing number."""


class PaymentMethodListResponse(BaseModel):
    employee_count: Optional[int] = FieldInfo(alias="employeeCount", default=None)
    """The total number of employees within the organization."""

    employees: Optional[List[Employee]] = None
    """List containing payment methods of employees within the organization."""
