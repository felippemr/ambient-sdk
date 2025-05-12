# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmployerCreateParams"]


class EmployerCreateParams(TypedDict, total=False):
    city: Required[str]
    """City where the employer is located."""

    ein: Required[str]
    """Employer Identification Number (EIN)."""

    employer_id: Required[Annotated[str, PropertyInfo(alias="employerId")]]
    """Unique identifier for the employer. Can be used as external identifier."""

    name: Required[str]
    """Name of the employer."""

    org_id: Required[Annotated[int, PropertyInfo(alias="orgId")]]
    """Organization identifier associated with the employer.

    Maps to id field of parent org.
    """

    state: Required[str]
    """State where the employer is located."""

    street_address1: Required[Annotated[str, PropertyInfo(alias="streetAddress1")]]
    """Primary street address of the employer."""

    zip: Required[str]
    """ZIP code for the employer's location."""

    street_address2: Annotated[str, PropertyInfo(alias="streetAddress2")]
    """Secondary street address of the employer (if applicable)."""
