# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmployeeArchiveParams"]


class EmployeeArchiveParams(TypedDict, total=False):
    id_type: Required[Annotated[str, PropertyInfo(alias="idType")]]

    admin_memo: Annotated[str, PropertyInfo(alias="adminMemo")]
    """A message attached to the archive."""

    archived_at: Annotated[Union[str, datetime], PropertyInfo(alias="archivedAt", format="iso8601")]
    """The date for the archive to take place."""

    archived_reason: Annotated[str, PropertyInfo(alias="archivedReason")]
    """The reason for the archive."""
