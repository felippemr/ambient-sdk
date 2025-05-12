# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["EmployerCreateBatchResponse", "EmployerCreateBatchResponseItem"]


class EmployerCreateBatchResponseItem(BaseModel):
    id: Optional[str] = None
    """The ID of the employer."""

    status: Optional[str] = None
    """The status of the employer creation."""


EmployerCreateBatchResponse: TypeAlias = List[EmployerCreateBatchResponseItem]
