# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["AuthorizationResource", "AsyncAuthorizationResource"]


class AuthorizationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthorizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felippemr/ambient-sdk#accessing-raw-response-data-eg-headers
        """
        return AuthorizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthorizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felippemr/ambient-sdk#with_streaming_response
        """
        return AuthorizationResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """All API requests must be authenticated.

        To get authorized, you must include a
        valid access token in the `Authorization`
        header:<br />`Authorization: Bearer < your_token >`
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/authorization",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncAuthorizationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthorizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felippemr/ambient-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthorizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthorizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felippemr/ambient-sdk#with_streaming_response
        """
        return AsyncAuthorizationResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """All API requests must be authenticated.

        To get authorized, you must include a
        valid access token in the `Authorization`
        header:<br />`Authorization: Bearer < your_token >`
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/authorization",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AuthorizationResourceWithRawResponse:
    def __init__(self, authorization: AuthorizationResource) -> None:
        self._authorization = authorization

        self.retrieve = to_raw_response_wrapper(
            authorization.retrieve,
        )


class AsyncAuthorizationResourceWithRawResponse:
    def __init__(self, authorization: AsyncAuthorizationResource) -> None:
        self._authorization = authorization

        self.retrieve = async_to_raw_response_wrapper(
            authorization.retrieve,
        )


class AuthorizationResourceWithStreamingResponse:
    def __init__(self, authorization: AuthorizationResource) -> None:
        self._authorization = authorization

        self.retrieve = to_streamed_response_wrapper(
            authorization.retrieve,
        )


class AsyncAuthorizationResourceWithStreamingResponse:
    def __init__(self, authorization: AsyncAuthorizationResource) -> None:
        self._authorization = authorization

        self.retrieve = async_to_streamed_response_wrapper(
            authorization.retrieve,
        )
