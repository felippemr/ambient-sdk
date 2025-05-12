# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .employer_core_param import EmployerCoreParam

__all__ = ["EmployerCreateBatchParams"]


class EmployerCreateBatchParams(TypedDict, total=False):
    body: Required[Iterable[EmployerCoreParam]]
