# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .queue_transaction import QueueTransaction

__all__ = ["TransactionBatchQueueResponse"]

TransactionBatchQueueResponse: TypeAlias = List[QueueTransaction]
