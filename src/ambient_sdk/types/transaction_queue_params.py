# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransactionQueueParams"]


class TransactionQueueParams(TypedDict, total=False):
    admin_memo: Annotated[str, PropertyInfo(alias="adminMemo")]
    """A message attached to the queued transaction."""

    amount: float
    """The amount of the transaction."""

    from_account: Annotated[str, PropertyInfo(alias="fromAccount")]
    """The passport account number associated with the transaction."""

    to_account: Annotated[str, PropertyInfo(alias="toAccount")]
    """The counterparty's passport account number associated with the transaction."""
