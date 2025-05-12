# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .employee_core_param import EmployeeCoreParam

__all__ = ["EmployeeBatchCreateParams"]


class EmployeeBatchCreateParams(TypedDict, total=False):
    body: Required[Iterable[EmployeeCoreParam]]
