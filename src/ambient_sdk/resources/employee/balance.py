# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.employee import balance_update_params
from ...types.employee.balance_update_response import BalanceUpdateResponse
from ...types.employee.balance_retrieve_response import BalanceRetrieveResponse

__all__ = ["BalanceResource", "AsyncBalanceResource"]


class BalanceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BalanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felippemr/ambient-sdk#accessing-raw-response-data-eg-headers
        """
        return BalanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BalanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felippemr/ambient-sdk#with_streaming_response
        """
        return BalanceResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        id_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BalanceRetrieveResponse:
        """
        Retrieve the balance information of an employee based on the specified ID type
        and ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_type:
            raise ValueError(f"Expected a non-empty value for `id_type` but received {id_type!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/employee/{id_type}/{id}/balance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BalanceRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        id_type: str,
        admin_memo: str | NotGiven = NOT_GIVEN,
        desired_amount: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BalanceUpdateResponse:
        """
        Queue a transaction that adjusts the balance of an employee based on the
        specified ID type and ID.

        Args:
          admin_memo: A message attached to the adjustment.

          desired_amount: The new desired balance of the employee.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_type:
            raise ValueError(f"Expected a non-empty value for `id_type` but received {id_type!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/employee/{id_type}/{id}/balance",
            body=maybe_transform(
                {
                    "admin_memo": admin_memo,
                    "desired_amount": desired_amount,
                },
                balance_update_params.BalanceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BalanceUpdateResponse,
        )


class AsyncBalanceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBalanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felippemr/ambient-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBalanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBalanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felippemr/ambient-sdk#with_streaming_response
        """
        return AsyncBalanceResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        id_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BalanceRetrieveResponse:
        """
        Retrieve the balance information of an employee based on the specified ID type
        and ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_type:
            raise ValueError(f"Expected a non-empty value for `id_type` but received {id_type!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/employee/{id_type}/{id}/balance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BalanceRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        id_type: str,
        admin_memo: str | NotGiven = NOT_GIVEN,
        desired_amount: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BalanceUpdateResponse:
        """
        Queue a transaction that adjusts the balance of an employee based on the
        specified ID type and ID.

        Args:
          admin_memo: A message attached to the adjustment.

          desired_amount: The new desired balance of the employee.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_type:
            raise ValueError(f"Expected a non-empty value for `id_type` but received {id_type!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/employee/{id_type}/{id}/balance",
            body=await async_maybe_transform(
                {
                    "admin_memo": admin_memo,
                    "desired_amount": desired_amount,
                },
                balance_update_params.BalanceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BalanceUpdateResponse,
        )


class BalanceResourceWithRawResponse:
    def __init__(self, balance: BalanceResource) -> None:
        self._balance = balance

        self.retrieve = to_raw_response_wrapper(
            balance.retrieve,
        )
        self.update = to_raw_response_wrapper(
            balance.update,
        )


class AsyncBalanceResourceWithRawResponse:
    def __init__(self, balance: AsyncBalanceResource) -> None:
        self._balance = balance

        self.retrieve = async_to_raw_response_wrapper(
            balance.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            balance.update,
        )


class BalanceResourceWithStreamingResponse:
    def __init__(self, balance: BalanceResource) -> None:
        self._balance = balance

        self.retrieve = to_streamed_response_wrapper(
            balance.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            balance.update,
        )


class AsyncBalanceResourceWithStreamingResponse:
    def __init__(self, balance: AsyncBalanceResource) -> None:
        self._balance = balance

        self.retrieve = async_to_streamed_response_wrapper(
            balance.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            balance.update,
        )
