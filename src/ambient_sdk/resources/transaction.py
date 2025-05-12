# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import transaction_queue_params, transaction_batch_queue_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.queue_transaction import QueueTransaction
from ..types.transaction_retrieve_response import TransactionRetrieveResponse
from ..types.transaction_batch_queue_response import TransactionBatchQueueResponse

__all__ = ["TransactionResource", "AsyncTransactionResource"]


class TransactionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransactionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felippemr/ambient-sdk#accessing-raw-response-data-eg-headers
        """
        return TransactionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felippemr/ambient-sdk#with_streaming_response
        """
        return TransactionResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionRetrieveResponse:
        """
        Retrieve the details of a transaction based on the specified transaction ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/transaction/id/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionRetrieveResponse,
        )

    def batch_queue(
        self,
        *,
        body: Iterable[transaction_batch_queue_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionBatchQueueResponse:
        """
        Queues a batch transactions to be processed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/transaction/batch",
            body=maybe_transform(body, Iterable[transaction_batch_queue_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionBatchQueueResponse,
        )

    def queue(
        self,
        *,
        admin_memo: str | NotGiven = NOT_GIVEN,
        amount: float | NotGiven = NOT_GIVEN,
        from_account: str | NotGiven = NOT_GIVEN,
        to_account: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueueTransaction:
        """
        Queue a transaction to be processed.

        Args:
          admin_memo: A message attached to the queued transaction.

          amount: The amount of the transaction.

          from_account: The passport account number associated with the transaction.

          to_account: The counterparty's passport account number associated with the transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/transaction",
            body=maybe_transform(
                {
                    "admin_memo": admin_memo,
                    "amount": amount,
                    "from_account": from_account,
                    "to_account": to_account,
                },
                transaction_queue_params.TransactionQueueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueueTransaction,
        )


class AsyncTransactionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransactionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felippemr/ambient-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTransactionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felippemr/ambient-sdk#with_streaming_response
        """
        return AsyncTransactionResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionRetrieveResponse:
        """
        Retrieve the details of a transaction based on the specified transaction ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/transaction/id/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionRetrieveResponse,
        )

    async def batch_queue(
        self,
        *,
        body: Iterable[transaction_batch_queue_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionBatchQueueResponse:
        """
        Queues a batch transactions to be processed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/transaction/batch",
            body=await async_maybe_transform(body, Iterable[transaction_batch_queue_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionBatchQueueResponse,
        )

    async def queue(
        self,
        *,
        admin_memo: str | NotGiven = NOT_GIVEN,
        amount: float | NotGiven = NOT_GIVEN,
        from_account: str | NotGiven = NOT_GIVEN,
        to_account: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueueTransaction:
        """
        Queue a transaction to be processed.

        Args:
          admin_memo: A message attached to the queued transaction.

          amount: The amount of the transaction.

          from_account: The passport account number associated with the transaction.

          to_account: The counterparty's passport account number associated with the transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/transaction",
            body=await async_maybe_transform(
                {
                    "admin_memo": admin_memo,
                    "amount": amount,
                    "from_account": from_account,
                    "to_account": to_account,
                },
                transaction_queue_params.TransactionQueueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueueTransaction,
        )


class TransactionResourceWithRawResponse:
    def __init__(self, transaction: TransactionResource) -> None:
        self._transaction = transaction

        self.retrieve = to_raw_response_wrapper(
            transaction.retrieve,
        )
        self.batch_queue = to_raw_response_wrapper(
            transaction.batch_queue,
        )
        self.queue = to_raw_response_wrapper(
            transaction.queue,
        )


class AsyncTransactionResourceWithRawResponse:
    def __init__(self, transaction: AsyncTransactionResource) -> None:
        self._transaction = transaction

        self.retrieve = async_to_raw_response_wrapper(
            transaction.retrieve,
        )
        self.batch_queue = async_to_raw_response_wrapper(
            transaction.batch_queue,
        )
        self.queue = async_to_raw_response_wrapper(
            transaction.queue,
        )


class TransactionResourceWithStreamingResponse:
    def __init__(self, transaction: TransactionResource) -> None:
        self._transaction = transaction

        self.retrieve = to_streamed_response_wrapper(
            transaction.retrieve,
        )
        self.batch_queue = to_streamed_response_wrapper(
            transaction.batch_queue,
        )
        self.queue = to_streamed_response_wrapper(
            transaction.queue,
        )


class AsyncTransactionResourceWithStreamingResponse:
    def __init__(self, transaction: AsyncTransactionResource) -> None:
        self._transaction = transaction

        self.retrieve = async_to_streamed_response_wrapper(
            transaction.retrieve,
        )
        self.batch_queue = async_to_streamed_response_wrapper(
            transaction.batch_queue,
        )
        self.queue = async_to_streamed_response_wrapper(
            transaction.queue,
        )
