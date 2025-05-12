# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .employee.employee import Employee

__all__ = ["ReportRetrieveArchivedAccountsReportResponse"]

ReportRetrieveArchivedAccountsReportResponse: TypeAlias = List[Employee]
