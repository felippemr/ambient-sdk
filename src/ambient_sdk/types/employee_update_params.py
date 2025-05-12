# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmployeeUpdateParams"]


class EmployeeUpdateParams(TypedDict, total=False):
    id_type: Required[Annotated[str, PropertyInfo(alias="idType")]]

    city: str
    """City where the employee resides."""

    debit_id: Annotated[str, PropertyInfo(alias="debitId")]
    """Unique identifier for the debit card."""

    dob: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Date of birth of the employee."""

    email: str
    """Email address of the employee."""

    employee_id: Annotated[str, PropertyInfo(alias="employeeId")]
    """Unique identifier for the employee in the system.

    Can be used as external identifier.
    """

    employer_id: Annotated[str, PropertyInfo(alias="employerId")]
    """Identifier for the employer associated with the employee.

    Can be used as external identifier. If provided, must match an existing
    employer's employerId.
    """

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """First name of the employee."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """Last name of the employee."""

    org_id: Annotated[int, PropertyInfo(alias="orgId")]
    """Organization identifier associated with the employee."""

    owner: bool
    """Flag indicating if the employee is an owner."""

    passport_account_id: Annotated[str, PropertyInfo(alias="passportAccountId")]
    """Account ID for passport processing."""

    passport_customer_id: Annotated[str, PropertyInfo(alias="passportCustomerId")]
    """Customer ID for passport processing."""

    phone: str
    """Contact phone number for the employee."""

    ssn: str
    """Social Security Number (SSN) of the employee."""

    state: str
    """State where the employee resides."""

    status: str
    """Current employment status of the employee."""

    street_address1: Annotated[str, PropertyInfo(alias="streetAddress1")]
    """Primary street address of the employee."""

    zip: str
    """ZIP code for the employee's residence."""
