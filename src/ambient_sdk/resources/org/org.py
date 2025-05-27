# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import org_create_params, org_update_params, org_list_transactions_params
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
from ...types.org.org import Org
from .employee.employee import (
    EmployeeResource,
    AsyncEmployeeResource,
    EmployeeResourceWithRawResponse,
    AsyncEmployeeResourceWithRawResponse,
    EmployeeResourceWithStreamingResponse,
    AsyncEmployeeResourceWithStreamingResponse,
)
from ...types.org_create_response import OrgCreateResponse
from ...types.org_update_response import OrgUpdateResponse
from ...types.org_retrieve_balance_response import OrgRetrieveBalanceResponse
from ...types.org_list_transactions_response import OrgListTransactionsResponse
from ...types.org_retrieve_bank_info_response import OrgRetrieveBankInfoResponse

__all__ = ["OrgResource", "AsyncOrgResource"]


class OrgResource(SyncAPIResource):
    @cached_property
    def employee(self) -> EmployeeResource:
        return EmployeeResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felippemr/ambient-sdk#accessing-raw-response-data-eg-headers
        """
        return OrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felippemr/ambient-sdk#with_streaming_response
        """
        return OrgResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        city: str,
        ein: str,
        name: str,
        state: str,
        street_address1: str,
        zip: str,
        parent: int | NotGiven = NOT_GIVEN,
        street_address2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgCreateResponse:
        """
        Creates new organization with given information, queing banking data creation.

        Args:
          city: City where the organization is located.

          ein: Employer Identification Number (EIN).

          name: Name of the organization.

          state: State where the organization is located.

          street_address1: Primary street address of the organization.

          zip: ZIP code for the organization's location.

          parent: ID of the parent organization (must be within same tree).

          street_address2: Secondary street address of the organization (if applicable).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/org",
            body=maybe_transform(
                {
                    "city": city,
                    "ein": ein,
                    "name": name,
                    "state": state,
                    "street_address1": street_address1,
                    "zip": zip,
                    "parent": parent,
                    "street_address2": street_address2,
                },
                org_create_params.OrgCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgCreateResponse,
        )

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
    ) -> Org:
        """
        Retrieve organization information based on the specified ID type and ID.

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
            f"/org/{id_type}/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Org,
        )

    def update(
        self,
        path_id: str,
        *,
        id_type: str,
        body_id: int | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        ein: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        passport_account_id: str | NotGiven = NOT_GIVEN,
        passport_customer_id: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        street_address1: str | NotGiven = NOT_GIVEN,
        street_address2: str | NotGiven = NOT_GIVEN,
        zip: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgUpdateResponse:
        """
        Update organization information based on the specified ID type and ID.

        Args:
          body_id: Unique identifier for the organization.

          city: City where the organization is located.

          ein: Employer Identification Number (EIN).

          name: Name of the organization.

          passport_account_id: Account ID for passport processing.

          passport_customer_id: Customer ID for passport processing.

          state: State where the organization is located.

          street_address1: Primary street address of the organization.

          street_address2: Secondary street address of the organization (if applicable).

          zip: ZIP code for the organization's location.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_type:
            raise ValueError(f"Expected a non-empty value for `id_type` but received {id_type!r}")
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return self._post(
            f"/org/{id_type}/{path_id}",
            body=maybe_transform(
                {
                    "body_id": body_id,
                    "city": city,
                    "ein": ein,
                    "name": name,
                    "passport_account_id": passport_account_id,
                    "passport_customer_id": passport_customer_id,
                    "state": state,
                    "street_address1": street_address1,
                    "street_address2": street_address2,
                    "zip": zip,
                },
                org_update_params.OrgUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgUpdateResponse,
        )

    def list_transactions(
        self,
        id: str,
        *,
        id_type: str,
        end_date: str,
        start_date: str,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgListTransactionsResponse:
        """
        Retrieve the list of transactions for an organization based on the specified ID
        type and ID.

        Args:
          end_date: The end date for filtering transactions in YYYY-MM-DD format (e.g.,
              "2025-01-01").

          start_date: The start date for filtering transactions in YYYY-MM-DD format (e.g.,
              "2024-02-01").

          limit: The number of rows to return.

          offset: The starting point from which rows are returned in the result.

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
            f"/org/{id_type}/{id}/transaction",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "limit": limit,
                        "offset": offset,
                    },
                    org_list_transactions_params.OrgListTransactionsParams,
                ),
            ),
            cast_to=OrgListTransactionsResponse,
        )

    def retrieve_balance(
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
    ) -> OrgRetrieveBalanceResponse:
        """
        Retrieve the balance information of an organization based on the specified ID
        type and ID.

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
            f"/org/{id_type}/{id}/balance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgRetrieveBalanceResponse,
        )

    def retrieve_bank_info(
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
    ) -> OrgRetrieveBankInfoResponse:
        """
        Retrieve the bank information of an organization based on the specified ID type
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
            f"/org/{id_type}/{id}/bank",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgRetrieveBankInfoResponse,
        )


class AsyncOrgResource(AsyncAPIResource):
    @cached_property
    def employee(self) -> AsyncEmployeeResource:
        return AsyncEmployeeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felippemr/ambient-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felippemr/ambient-sdk#with_streaming_response
        """
        return AsyncOrgResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        city: str,
        ein: str,
        name: str,
        state: str,
        street_address1: str,
        zip: str,
        parent: int | NotGiven = NOT_GIVEN,
        street_address2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgCreateResponse:
        """
        Creates new organization with given information, queing banking data creation.

        Args:
          city: City where the organization is located.

          ein: Employer Identification Number (EIN).

          name: Name of the organization.

          state: State where the organization is located.

          street_address1: Primary street address of the organization.

          zip: ZIP code for the organization's location.

          parent: ID of the parent organization (must be within same tree).

          street_address2: Secondary street address of the organization (if applicable).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/org",
            body=await async_maybe_transform(
                {
                    "city": city,
                    "ein": ein,
                    "name": name,
                    "state": state,
                    "street_address1": street_address1,
                    "zip": zip,
                    "parent": parent,
                    "street_address2": street_address2,
                },
                org_create_params.OrgCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgCreateResponse,
        )

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
    ) -> Org:
        """
        Retrieve organization information based on the specified ID type and ID.

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
            f"/org/{id_type}/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Org,
        )

    async def update(
        self,
        path_id: str,
        *,
        id_type: str,
        body_id: int | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        ein: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        passport_account_id: str | NotGiven = NOT_GIVEN,
        passport_customer_id: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        street_address1: str | NotGiven = NOT_GIVEN,
        street_address2: str | NotGiven = NOT_GIVEN,
        zip: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgUpdateResponse:
        """
        Update organization information based on the specified ID type and ID.

        Args:
          body_id: Unique identifier for the organization.

          city: City where the organization is located.

          ein: Employer Identification Number (EIN).

          name: Name of the organization.

          passport_account_id: Account ID for passport processing.

          passport_customer_id: Customer ID for passport processing.

          state: State where the organization is located.

          street_address1: Primary street address of the organization.

          street_address2: Secondary street address of the organization (if applicable).

          zip: ZIP code for the organization's location.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id_type:
            raise ValueError(f"Expected a non-empty value for `id_type` but received {id_type!r}")
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return await self._post(
            f"/org/{id_type}/{path_id}",
            body=await async_maybe_transform(
                {
                    "body_id": body_id,
                    "city": city,
                    "ein": ein,
                    "name": name,
                    "passport_account_id": passport_account_id,
                    "passport_customer_id": passport_customer_id,
                    "state": state,
                    "street_address1": street_address1,
                    "street_address2": street_address2,
                    "zip": zip,
                },
                org_update_params.OrgUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgUpdateResponse,
        )

    async def list_transactions(
        self,
        id: str,
        *,
        id_type: str,
        end_date: str,
        start_date: str,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgListTransactionsResponse:
        """
        Retrieve the list of transactions for an organization based on the specified ID
        type and ID.

        Args:
          end_date: The end date for filtering transactions in YYYY-MM-DD format (e.g.,
              "2025-01-01").

          start_date: The start date for filtering transactions in YYYY-MM-DD format (e.g.,
              "2024-02-01").

          limit: The number of rows to return.

          offset: The starting point from which rows are returned in the result.

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
            f"/org/{id_type}/{id}/transaction",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "limit": limit,
                        "offset": offset,
                    },
                    org_list_transactions_params.OrgListTransactionsParams,
                ),
            ),
            cast_to=OrgListTransactionsResponse,
        )

    async def retrieve_balance(
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
    ) -> OrgRetrieveBalanceResponse:
        """
        Retrieve the balance information of an organization based on the specified ID
        type and ID.

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
            f"/org/{id_type}/{id}/balance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgRetrieveBalanceResponse,
        )

    async def retrieve_bank_info(
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
    ) -> OrgRetrieveBankInfoResponse:
        """
        Retrieve the bank information of an organization based on the specified ID type
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
            f"/org/{id_type}/{id}/bank",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgRetrieveBankInfoResponse,
        )


class OrgResourceWithRawResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

        self.create = to_raw_response_wrapper(
            org.create,
        )
        self.retrieve = to_raw_response_wrapper(
            org.retrieve,
        )
        self.update = to_raw_response_wrapper(
            org.update,
        )
        self.list_transactions = to_raw_response_wrapper(
            org.list_transactions,
        )
        self.retrieve_balance = to_raw_response_wrapper(
            org.retrieve_balance,
        )
        self.retrieve_bank_info = to_raw_response_wrapper(
            org.retrieve_bank_info,
        )

    @cached_property
    def employee(self) -> EmployeeResourceWithRawResponse:
        return EmployeeResourceWithRawResponse(self._org.employee)


class AsyncOrgResourceWithRawResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

        self.create = async_to_raw_response_wrapper(
            org.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            org.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            org.update,
        )
        self.list_transactions = async_to_raw_response_wrapper(
            org.list_transactions,
        )
        self.retrieve_balance = async_to_raw_response_wrapper(
            org.retrieve_balance,
        )
        self.retrieve_bank_info = async_to_raw_response_wrapper(
            org.retrieve_bank_info,
        )

    @cached_property
    def employee(self) -> AsyncEmployeeResourceWithRawResponse:
        return AsyncEmployeeResourceWithRawResponse(self._org.employee)


class OrgResourceWithStreamingResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

        self.create = to_streamed_response_wrapper(
            org.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            org.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            org.update,
        )
        self.list_transactions = to_streamed_response_wrapper(
            org.list_transactions,
        )
        self.retrieve_balance = to_streamed_response_wrapper(
            org.retrieve_balance,
        )
        self.retrieve_bank_info = to_streamed_response_wrapper(
            org.retrieve_bank_info,
        )

    @cached_property
    def employee(self) -> EmployeeResourceWithStreamingResponse:
        return EmployeeResourceWithStreamingResponse(self._org.employee)


class AsyncOrgResourceWithStreamingResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

        self.create = async_to_streamed_response_wrapper(
            org.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            org.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            org.update,
        )
        self.list_transactions = async_to_streamed_response_wrapper(
            org.list_transactions,
        )
        self.retrieve_balance = async_to_streamed_response_wrapper(
            org.retrieve_balance,
        )
        self.retrieve_bank_info = async_to_streamed_response_wrapper(
            org.retrieve_bank_info,
        )

    @cached_property
    def employee(self) -> AsyncEmployeeResourceWithStreamingResponse:
        return AsyncEmployeeResourceWithStreamingResponse(self._org.employee)
