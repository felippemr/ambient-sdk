# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .payment_methods import (
    PaymentMethodsResource,
    AsyncPaymentMethodsResource,
    PaymentMethodsResourceWithRawResponse,
    AsyncPaymentMethodsResourceWithRawResponse,
    PaymentMethodsResourceWithStreamingResponse,
    AsyncPaymentMethodsResourceWithStreamingResponse,
)

__all__ = ["EmployeeResource", "AsyncEmployeeResource"]


class EmployeeResource(SyncAPIResource):
    @cached_property
    def payment_methods(self) -> PaymentMethodsResource:
        return PaymentMethodsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmployeeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felippemr/ambient-sdk#accessing-raw-response-data-eg-headers
        """
        return EmployeeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmployeeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felippemr/ambient-sdk#with_streaming_response
        """
        return EmployeeResourceWithStreamingResponse(self)


class AsyncEmployeeResource(AsyncAPIResource):
    @cached_property
    def payment_methods(self) -> AsyncPaymentMethodsResource:
        return AsyncPaymentMethodsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmployeeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felippemr/ambient-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEmployeeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmployeeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felippemr/ambient-sdk#with_streaming_response
        """
        return AsyncEmployeeResourceWithStreamingResponse(self)


class EmployeeResourceWithRawResponse:
    def __init__(self, employee: EmployeeResource) -> None:
        self._employee = employee

    @cached_property
    def payment_methods(self) -> PaymentMethodsResourceWithRawResponse:
        return PaymentMethodsResourceWithRawResponse(self._employee.payment_methods)


class AsyncEmployeeResourceWithRawResponse:
    def __init__(self, employee: AsyncEmployeeResource) -> None:
        self._employee = employee

    @cached_property
    def payment_methods(self) -> AsyncPaymentMethodsResourceWithRawResponse:
        return AsyncPaymentMethodsResourceWithRawResponse(self._employee.payment_methods)


class EmployeeResourceWithStreamingResponse:
    def __init__(self, employee: EmployeeResource) -> None:
        self._employee = employee

    @cached_property
    def payment_methods(self) -> PaymentMethodsResourceWithStreamingResponse:
        return PaymentMethodsResourceWithStreamingResponse(self._employee.payment_methods)


class AsyncEmployeeResourceWithStreamingResponse:
    def __init__(self, employee: AsyncEmployeeResource) -> None:
        self._employee = employee

    @cached_property
    def payment_methods(self) -> AsyncPaymentMethodsResourceWithStreamingResponse:
        return AsyncPaymentMethodsResourceWithStreamingResponse(self._employee.payment_methods)
