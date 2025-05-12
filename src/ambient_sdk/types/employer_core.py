# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmployerCore"]


class EmployerCore(BaseModel):
    city: str
    """City where the employer is located."""

    ein: str
    """Employer Identification Number (EIN)."""

    employer_id: str = FieldInfo(alias="employerId")
    """Unique identifier for the employer. Can be used as external identifier."""

    name: str
    """Name of the employer."""

    org_id: int = FieldInfo(alias="orgId")
    """Organization identifier associated with the employer.

    Maps to id field of parent org.
    """

    state: str
    """State where the employer is located."""

    street_address1: str = FieldInfo(alias="streetAddress1")
    """Primary street address of the employer."""

    zip: str
    """ZIP code for the employer's location."""

    street_address2: Optional[str] = FieldInfo(alias="streetAddress2", default=None)
    """Secondary street address of the employer (if applicable)."""
