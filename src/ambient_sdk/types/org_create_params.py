# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrgCreateParams"]


class OrgCreateParams(TypedDict, total=False):
    city: Required[str]
    """City where the organization is located."""

    ein: Required[str]
    """Employer Identification Number (EIN)."""

    name: Required[str]
    """Name of the organization."""

    state: Required[str]
    """State where the organization is located."""

    street_address1: Required[Annotated[str, PropertyInfo(alias="streetAddress1")]]
    """Primary street address of the organization."""

    zip: Required[str]
    """ZIP code for the organization's location."""

    parent: int
    """ID of the parent organization (must be within same tree)."""

    street_address2: Annotated[str, PropertyInfo(alias="streetAddress2")]
    """Secondary street address of the organization (if applicable)."""
