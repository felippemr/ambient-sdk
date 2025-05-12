# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["EmployeeBatchCreateResponse", "EmployeeBatchCreateResponseItem"]


class EmployeeBatchCreateResponseItem(BaseModel):
    id: Optional[str] = None
    """The ID of the employee."""

    status: Optional[str] = None
    """The status of the employee creation."""


EmployeeBatchCreateResponse: TypeAlias = List[EmployeeBatchCreateResponseItem]
