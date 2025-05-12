# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ReportRetrieveNonzeroBalanceAccountsReportParams"]


class ReportRetrieveNonzeroBalanceAccountsReportParams(TypedDict, total=False):
    employer_id: Annotated[str, PropertyInfo(alias="employerId")]
    """
    A comma-separated list of employer IDs to filter the accounts with non-zero
    balance.
    """
