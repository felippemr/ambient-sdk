# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PaymentMethodListParams"]


class PaymentMethodListParams(TypedDict, total=False):
    id_type: Required[Annotated[str, PropertyInfo(alias="idType")]]

    page: int
    """The page number for pagination (default is 0)."""
