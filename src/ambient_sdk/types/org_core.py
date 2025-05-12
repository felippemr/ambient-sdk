# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OrgCore"]


class OrgCore(BaseModel):
    city: str
    """City where the organization is located."""

    ein: str
    """Employer Identification Number (EIN)."""

    name: str
    """Name of the organization."""

    state: str
    """State where the organization is located."""

    street_address1: str = FieldInfo(alias="streetAddress1")
    """Primary street address of the organization."""

    zip: str
    """ZIP code for the organization's location."""

    parent: Optional[int] = None
    """ID of the parent organization (must be within same tree)."""

    street_address2: Optional[str] = FieldInfo(alias="streetAddress2", default=None)
    """Secondary street address of the organization (if applicable)."""
