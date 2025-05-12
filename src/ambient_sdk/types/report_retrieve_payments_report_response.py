# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ReportRetrievePaymentsReportResponse", "ReportRetrievePaymentsReportResponseItem"]


class ReportRetrievePaymentsReportResponseItem(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the transaction."""

    amount: Optional[float] = None
    """The amount of the transaction."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time when the transaction was created."""

    employee_id: Optional[str] = FieldInfo(alias="employeeId", default=None)
    """The ID of the employee associated with the transaction."""

    employer_id: Optional[str] = FieldInfo(alias="employerId", default=None)
    """The ID of the employer associated with the transaction."""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """The first name of the employee."""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The last name of the employee."""

    message: Optional[str] = None
    """The message attached to the transaction."""

    passport_account_id: Optional[str] = FieldInfo(alias="passportAccountId", default=None)
    """The passport account ID associated with the transaction."""

    type_text: Optional[str] = FieldInfo(alias="typeText", default=None)
    """The type of transactions to filter (e.g., "card" or "ach")."""


ReportRetrievePaymentsReportResponse: TypeAlias = List[ReportRetrievePaymentsReportResponseItem]
