# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmployerUpdateParams"]


class EmployerUpdateParams(TypedDict, total=False):
    id_type: Required[Annotated[str, PropertyInfo(alias="idType")]]

    city: str
    """City where the employer is located."""

    dba: str
    """'Doing Business As' name for the employer."""

    ein: str
    """Employer Identification Number (EIN)."""

    employer_id: Annotated[str, PropertyInfo(alias="employerId")]
    """Unique identifier for the employer. Can be used as external identifier."""

    name: str
    """Name of the employer."""

    org_id: Annotated[int, PropertyInfo(alias="orgId")]
    """Organization identifier associated with the employer.

    Maps to id field of parent org.
    """

    passport_account_id: Annotated[str, PropertyInfo(alias="passportAccountId")]
    """Account ID for passport processing."""

    passport_customer_id: Annotated[str, PropertyInfo(alias="passportCustomerId")]
    """Customer ID for passport processing."""

    state: str
    """State where the employer is located."""

    street_address1: Annotated[str, PropertyInfo(alias="streetAddress1")]
    """Primary street address of the employer."""

    street_address2: Annotated[str, PropertyInfo(alias="streetAddress2")]
    """Secondary street address of the employer (if applicable)."""

    zip: str
    """ZIP code for the employer's location."""
