# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import (
    employer_create_params,
    employer_update_params,
    employer_list_transactions_params,
)
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
from ..types.employer_core_param import EmployerCoreParam
from ..types.employer_create_response import EmployerCreateResponse
from ..types.employer_update_response import EmployerUpdateResponse
from ..types.employer_retrieve_response import EmployerRetrieveResponse
from ..types.employer_create_batch_response import EmployerCreateBatchResponse
from ..types.employer_retrieve_balance_response import EmployerRetrieveBalanceResponse
from ..types.employer_list_transactions_response import EmployerListTransactionsResponse
from ..types.employer_retrieve_bank_info_response import EmployerRetrieveBankInfoResponse

__all__ = ["EmployerResource", "AsyncEmployerResource"]


class EmployerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmployerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felippemr/ambient-sdk#accessing-raw-response-data-eg-headers
        """
        return EmployerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmployerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felippemr/ambient-sdk#with_streaming_response
        """
        return EmployerResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        city: str,
        ein: str,
        employer_id: str,
        name: str,
        org_id: int,
        state: str,
        street_address1: str,
        zip: str,
        street_address2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployerCreateResponse:
        """
        Creates new employer with given information, queing banking data creation.

        Args:
          city: City where the employer is located.

          ein: Employer Identification Number (EIN).

          employer_id: Unique identifier for the employer. Can be used as external identifier.

          name: Name of the employer.

          org_id: Organization identifier associated with the employer. Maps to id field of parent
              org.

          state: State where the employer is located.

          street_address1: Primary street address of the employer.

          zip: ZIP code for the employer's location.

          street_address2: Secondary street address of the employer (if applicable).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/employer",
            body=maybe_transform(
                {
                    "city": city,
                    "ein": ein,
                    "employer_id": employer_id,
                    "name": name,
                    "org_id": org_id,
                    "state": state,
                    "street_address1": street_address1,
                    "zip": zip,
                    "street_address2": street_address2,
                },
                employer_create_params.EmployerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerCreateResponse,
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
    ) -> EmployerRetrieveResponse:
        """
        Retrieve employer information based on the specified ID type and ID.

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
            f"/employer/{id_type}/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        id_type: str,
        city: str | NotGiven = NOT_GIVEN,
        dba: str | NotGiven = NOT_GIVEN,
        ein: str | NotGiven = NOT_GIVEN,
        employer_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        org_id: int | NotGiven = NOT_GIVEN,
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
    ) -> EmployerUpdateResponse:
        """
        Update employer information based on the specified ID type and ID.

        Args:
          city: City where the employer is located.

          dba: 'Doing Business As' name for the employer.

          ein: Employer Identification Number (EIN).

          employer_id: Unique identifier for the employer. Can be used as external identifier.

          name: Name of the employer.

          org_id: Organization identifier associated with the employer. Maps to id field of parent
              org.

          passport_account_id: Account ID for passport processing.

          passport_customer_id: Customer ID for passport processing.

          state: State where the employer is located.

          street_address1: Primary street address of the employer.

          street_address2: Secondary street address of the employer (if applicable).

          zip: ZIP code for the employer's location.

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
            f"/employer/{id_type}/{id}",
            body=maybe_transform(
                {
                    "city": city,
                    "dba": dba,
                    "ein": ein,
                    "employer_id": employer_id,
                    "name": name,
                    "org_id": org_id,
                    "passport_account_id": passport_account_id,
                    "passport_customer_id": passport_customer_id,
                    "state": state,
                    "street_address1": street_address1,
                    "street_address2": street_address2,
                    "zip": zip,
                },
                employer_update_params.EmployerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerUpdateResponse,
        )

    def create_batch(
        self,
        *,
        body: Iterable[EmployerCoreParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployerCreateBatchResponse:
        """
        Submits employer basic information in a list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/employer/batch",
            body=maybe_transform(body, Iterable[EmployerCoreParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerCreateBatchResponse,
        )

    def list_transactions(
        self,
        id: str,
        *,
        id_type: str,
        end_date: str,
        start_date: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployerListTransactionsResponse:
        """
        Retrieve the list of transactions for an employer based on the specified ID type
        and ID.

        Args:
          end_date: The end date for filtering transactions in YYYY-MM-DD format (e.g.,
              "2025-01-01").

          start_date: The start date for filtering transactions in YYYY-MM-DD format (e.g.,
              "2024-02-01").

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
            f"/employer/{id_type}/{id}/transaction",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    employer_list_transactions_params.EmployerListTransactionsParams,
                ),
            ),
            cast_to=EmployerListTransactionsResponse,
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
    ) -> EmployerRetrieveBalanceResponse:
        """
        Retrieve the balance information of an employer based on the specified ID type
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
            f"/employer/{id_type}/{id}/balance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerRetrieveBalanceResponse,
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
    ) -> EmployerRetrieveBankInfoResponse:
        """
        Retrieve the bank information of an employer based on the specified ID type and
        ID.

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
            f"/employer/{id_type}/{id}/bank",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerRetrieveBankInfoResponse,
        )


class AsyncEmployerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmployerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felippemr/ambient-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEmployerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmployerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felippemr/ambient-sdk#with_streaming_response
        """
        return AsyncEmployerResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        city: str,
        ein: str,
        employer_id: str,
        name: str,
        org_id: int,
        state: str,
        street_address1: str,
        zip: str,
        street_address2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployerCreateResponse:
        """
        Creates new employer with given information, queing banking data creation.

        Args:
          city: City where the employer is located.

          ein: Employer Identification Number (EIN).

          employer_id: Unique identifier for the employer. Can be used as external identifier.

          name: Name of the employer.

          org_id: Organization identifier associated with the employer. Maps to id field of parent
              org.

          state: State where the employer is located.

          street_address1: Primary street address of the employer.

          zip: ZIP code for the employer's location.

          street_address2: Secondary street address of the employer (if applicable).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/employer",
            body=await async_maybe_transform(
                {
                    "city": city,
                    "ein": ein,
                    "employer_id": employer_id,
                    "name": name,
                    "org_id": org_id,
                    "state": state,
                    "street_address1": street_address1,
                    "zip": zip,
                    "street_address2": street_address2,
                },
                employer_create_params.EmployerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerCreateResponse,
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
    ) -> EmployerRetrieveResponse:
        """
        Retrieve employer information based on the specified ID type and ID.

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
            f"/employer/{id_type}/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        id_type: str,
        city: str | NotGiven = NOT_GIVEN,
        dba: str | NotGiven = NOT_GIVEN,
        ein: str | NotGiven = NOT_GIVEN,
        employer_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        org_id: int | NotGiven = NOT_GIVEN,
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
    ) -> EmployerUpdateResponse:
        """
        Update employer information based on the specified ID type and ID.

        Args:
          city: City where the employer is located.

          dba: 'Doing Business As' name for the employer.

          ein: Employer Identification Number (EIN).

          employer_id: Unique identifier for the employer. Can be used as external identifier.

          name: Name of the employer.

          org_id: Organization identifier associated with the employer. Maps to id field of parent
              org.

          passport_account_id: Account ID for passport processing.

          passport_customer_id: Customer ID for passport processing.

          state: State where the employer is located.

          street_address1: Primary street address of the employer.

          street_address2: Secondary street address of the employer (if applicable).

          zip: ZIP code for the employer's location.

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
            f"/employer/{id_type}/{id}",
            body=await async_maybe_transform(
                {
                    "city": city,
                    "dba": dba,
                    "ein": ein,
                    "employer_id": employer_id,
                    "name": name,
                    "org_id": org_id,
                    "passport_account_id": passport_account_id,
                    "passport_customer_id": passport_customer_id,
                    "state": state,
                    "street_address1": street_address1,
                    "street_address2": street_address2,
                    "zip": zip,
                },
                employer_update_params.EmployerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerUpdateResponse,
        )

    async def create_batch(
        self,
        *,
        body: Iterable[EmployerCoreParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployerCreateBatchResponse:
        """
        Submits employer basic information in a list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/employer/batch",
            body=await async_maybe_transform(body, Iterable[EmployerCoreParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerCreateBatchResponse,
        )

    async def list_transactions(
        self,
        id: str,
        *,
        id_type: str,
        end_date: str,
        start_date: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployerListTransactionsResponse:
        """
        Retrieve the list of transactions for an employer based on the specified ID type
        and ID.

        Args:
          end_date: The end date for filtering transactions in YYYY-MM-DD format (e.g.,
              "2025-01-01").

          start_date: The start date for filtering transactions in YYYY-MM-DD format (e.g.,
              "2024-02-01").

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
            f"/employer/{id_type}/{id}/transaction",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    employer_list_transactions_params.EmployerListTransactionsParams,
                ),
            ),
            cast_to=EmployerListTransactionsResponse,
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
    ) -> EmployerRetrieveBalanceResponse:
        """
        Retrieve the balance information of an employer based on the specified ID type
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
            f"/employer/{id_type}/{id}/balance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerRetrieveBalanceResponse,
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
    ) -> EmployerRetrieveBankInfoResponse:
        """
        Retrieve the bank information of an employer based on the specified ID type and
        ID.

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
            f"/employer/{id_type}/{id}/bank",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerRetrieveBankInfoResponse,
        )


class EmployerResourceWithRawResponse:
    def __init__(self, employer: EmployerResource) -> None:
        self._employer = employer

        self.create = to_raw_response_wrapper(
            employer.create,
        )
        self.retrieve = to_raw_response_wrapper(
            employer.retrieve,
        )
        self.update = to_raw_response_wrapper(
            employer.update,
        )
        self.create_batch = to_raw_response_wrapper(
            employer.create_batch,
        )
        self.list_transactions = to_raw_response_wrapper(
            employer.list_transactions,
        )
        self.retrieve_balance = to_raw_response_wrapper(
            employer.retrieve_balance,
        )
        self.retrieve_bank_info = to_raw_response_wrapper(
            employer.retrieve_bank_info,
        )


class AsyncEmployerResourceWithRawResponse:
    def __init__(self, employer: AsyncEmployerResource) -> None:
        self._employer = employer

        self.create = async_to_raw_response_wrapper(
            employer.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            employer.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            employer.update,
        )
        self.create_batch = async_to_raw_response_wrapper(
            employer.create_batch,
        )
        self.list_transactions = async_to_raw_response_wrapper(
            employer.list_transactions,
        )
        self.retrieve_balance = async_to_raw_response_wrapper(
            employer.retrieve_balance,
        )
        self.retrieve_bank_info = async_to_raw_response_wrapper(
            employer.retrieve_bank_info,
        )


class EmployerResourceWithStreamingResponse:
    def __init__(self, employer: EmployerResource) -> None:
        self._employer = employer

        self.create = to_streamed_response_wrapper(
            employer.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            employer.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            employer.update,
        )
        self.create_batch = to_streamed_response_wrapper(
            employer.create_batch,
        )
        self.list_transactions = to_streamed_response_wrapper(
            employer.list_transactions,
        )
        self.retrieve_balance = to_streamed_response_wrapper(
            employer.retrieve_balance,
        )
        self.retrieve_bank_info = to_streamed_response_wrapper(
            employer.retrieve_bank_info,
        )


class AsyncEmployerResourceWithStreamingResponse:
    def __init__(self, employer: AsyncEmployerResource) -> None:
        self._employer = employer

        self.create = async_to_streamed_response_wrapper(
            employer.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            employer.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            employer.update,
        )
        self.create_batch = async_to_streamed_response_wrapper(
            employer.create_batch,
        )
        self.list_transactions = async_to_streamed_response_wrapper(
            employer.list_transactions,
        )
        self.retrieve_balance = async_to_streamed_response_wrapper(
            employer.retrieve_balance,
        )
        self.retrieve_bank_info = async_to_streamed_response_wrapper(
            employer.retrieve_bank_info,
        )
