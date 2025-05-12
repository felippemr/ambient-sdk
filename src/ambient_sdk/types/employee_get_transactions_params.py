# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmployeeGetTransactionsParams"]


class EmployeeGetTransactionsParams(TypedDict, total=False):
    id_type: Required[Annotated[str, PropertyInfo(alias="idType")]]

    end_date: Required[Annotated[str, PropertyInfo(alias="endDate")]]
    """
    The end date for filtering transactions in YYYY-MM-DD format (e.g.,
    "2025-01-01").
    """

    start_date: Required[Annotated[str, PropertyInfo(alias="startDate")]]
    """
    The start date for filtering transactions in YYYY-MM-DD format (e.g.,
    "2024-02-01").
    """
