# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ReportRetrieveFundingTransferDetailReportResponse", "ReportRetrieveFundingTransferDetailReportResponseItem"]


class ReportRetrieveFundingTransferDetailReportResponseItem(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the transaction."""

    amount: Optional[float] = None
    """The amount of the transaction."""

    balance: Optional[float] = None
    """The balance of the employer's account after the transaction."""

    counterparty: Optional[str] = None
    """The passport account ID of the counterparty associated with the transaction."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time when the transaction was created."""

    employer_id: Optional[str] = FieldInfo(alias="employerId", default=None)
    """The ID of the employer associated with the transaction."""

    message: Optional[str] = None
    """The message attached to the transaction."""

    name: Optional[str] = None
    """The name of employer associated with the transaction."""

    passport_account_id: Optional[str] = FieldInfo(alias="passportAccountId", default=None)
    """The passport account ID associated with the transaction."""

    type_text: Optional[str] = FieldInfo(alias="typeText", default=None)
    """The type of transactions to filter (e.g., "card" or "ach")."""


ReportRetrieveFundingTransferDetailReportResponse: TypeAlias = List[
    ReportRetrieveFundingTransferDetailReportResponseItem
]
