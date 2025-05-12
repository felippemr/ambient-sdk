# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmployeeCreateParams"]


class EmployeeCreateParams(TypedDict, total=False):
    city: Required[str]
    """City where the employee resides."""

    dob: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Date of birth of the employee."""

    email: Required[str]
    """Email address of the employee."""

    employee_id: Required[Annotated[str, PropertyInfo(alias="employeeId")]]
    """Unique identifier for the employee in the system.

    Can be used as external identifier.
    """

    employer_id: Required[Annotated[str, PropertyInfo(alias="employerId")]]
    """Identifier for the employer associated with the employee.

    Can be used as external identifier. If provided, must match an existing
    employer's employerId.
    """

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]
    """First name of the employee."""

    last_name: Required[Annotated[str, PropertyInfo(alias="lastName")]]
    """Last name of the employee."""

    org_id: Required[Annotated[int, PropertyInfo(alias="orgId")]]
    """Organization identifier associated with the employee."""

    phone: Required[str]
    """Contact phone number for the employee."""

    ssn: Required[str]
    """Social Security Number (SSN) of the employee."""

    state: Required[str]
    """State where the employee resides."""

    street_address1: Required[Annotated[str, PropertyInfo(alias="streetAddress1")]]
    """Primary street address of the employee."""

    zip: Required[str]
    """ZIP code for the employee's residence."""

    middle_name: Annotated[str, PropertyInfo(alias="middleName")]
    """Middle name of the employee."""
