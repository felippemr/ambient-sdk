# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmployeeCore"]


class EmployeeCore(BaseModel):
    city: str
    """City where the employee resides."""

    dob: date
    """Date of birth of the employee."""

    email: str
    """Email address of the employee."""

    employee_id: str = FieldInfo(alias="employeeId")
    """Unique identifier for the employee in the system.

    Can be used as external identifier.
    """

    employer_id: str = FieldInfo(alias="employerId")
    """Identifier for the employer associated with the employee.

    Can be used as external identifier. If provided, must match an existing
    employer's employerId.
    """

    first_name: str = FieldInfo(alias="firstName")
    """First name of the employee."""

    last_name: str = FieldInfo(alias="lastName")
    """Last name of the employee."""

    org_id: int = FieldInfo(alias="orgId")
    """Organization identifier associated with the employee."""

    phone: str
    """Contact phone number for the employee."""

    ssn: str
    """Social Security Number (SSN) of the employee."""

    state: str
    """State where the employee resides."""

    street_address1: str = FieldInfo(alias="streetAddress1")
    """Primary street address of the employee."""

    zip: str
    """ZIP code for the employee's residence."""

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)
    """Middle name of the employee."""
