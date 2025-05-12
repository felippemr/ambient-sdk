# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ReportRetrieveFundingTransferDetailReportParams"]


class ReportRetrieveFundingTransferDetailReportParams(TypedDict, total=False):
    employer_id: Annotated[str, PropertyInfo(alias="employerId")]
    """A comma-separated list of employer IDs to filter the funding transfers."""

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """The end date for filtering transactions (e.g., "03-25-2024")."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """The start date for filtering transactions (e.g., "03-20-2024")."""
