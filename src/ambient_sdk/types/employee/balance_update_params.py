# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BalanceUpdateParams"]


class BalanceUpdateParams(TypedDict, total=False):
    id_type: Required[Annotated[str, PropertyInfo(alias="idType")]]

    admin_memo: Annotated[str, PropertyInfo(alias="adminMemo")]
    """A message attached to the adjustment."""

    desired_amount: Annotated[float, PropertyInfo(alias="desiredAmount")]
    """The new desired balance of the employee."""
