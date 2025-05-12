# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrgUpdateParams"]


class OrgUpdateParams(TypedDict, total=False):
    id_type: Required[Annotated[str, PropertyInfo(alias="idType")]]

    body_id: Annotated[int, PropertyInfo(alias="id")]
    """Unique identifier for the organization."""

    city: str
    """City where the organization is located."""

    ein: str
    """Employer Identification Number (EIN)."""

    name: str
    """Name of the organization."""

    passport_account_id: Annotated[str, PropertyInfo(alias="passportAccountId")]
    """Account ID for passport processing."""

    passport_customer_id: Annotated[str, PropertyInfo(alias="passportCustomerId")]
    """Customer ID for passport processing."""

    state: str
    """State where the organization is located."""

    street_address1: Annotated[str, PropertyInfo(alias="streetAddress1")]
    """Primary street address of the organization."""

    street_address2: Annotated[str, PropertyInfo(alias="streetAddress2")]
    """Secondary street address of the organization (if applicable)."""

    zip: str
    """ZIP code for the organization's location."""
