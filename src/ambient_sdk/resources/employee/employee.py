# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date, datetime

import httpx

from ...types import (
    employee_create_params,
    employee_update_params,
    employee_archive_params,
    employee_get_transactions_params,
)
from .balance import (
    BalanceResource,
    AsyncBalanceResource,
    BalanceResourceWithRawResponse,
    AsyncBalanceResourceWithRawResponse,
    BalanceResourceWithStreamingResponse,
    AsyncBalanceResourceWithStreamingResponse,
)
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
from ...types.employee.employee import Employee
from ...types.employee_core_param import EmployeeCoreParam
from ...types.employee_create_response import EmployeeCreateResponse
from ...types.employee_update_response import EmployeeUpdateResponse
from ...types.employee_archive_response import EmployeeArchiveResponse
from ...types.employee_unarchive_response import EmployeeUnarchiveResponse
from ...types.employee_batch_create_response import EmployeeBatchCreateResponse
from ...types.employee_get_transactions_response import EmployeeGetTransactionsResponse
from ...types.employee_get_payment_methods_response import EmployeeGetPaymentMethodsResponse

__all__ = ["EmployeeResource", "AsyncEmployeeResource"]


class EmployeeResource(SyncAPIResource):
    @cached_property
    def balance(self) -> BalanceResource:
        return BalanceResource(self._client)

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

    def create(
        self,
        *,
        city: str,
        dob: Union[str, date],
        email: str,
        employee_id: str,
        employer_id: str,
        first_name: str,
        last_name: str,
        org_id: int,
        phone: str,
        ssn: str,
        state: str,
        street_address1: str,
        zip: str,
        middle_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployeeCreateResponse:
        """
        Submits employee basic information and returns the complete employee record.

        Args:
          city: City where the employee resides.

          dob: Date of birth of the employee.

          email: Email address of the employee.

          employee_id: Unique identifier for the employee in the system. Can be used as external
              identifier.

          employer_id: Identifier for the employer associated with the employee. Can be used as
              external identifier. If provided, must match an existing employer's employerId.

          first_name: First name of the employee.

          last_name: Last name of the employee.

          org_id: Organization identifier associated with the employee.

          phone: Contact phone number for the employee.

          ssn: Social Security Number (SSN) of the employee.

          state: State where the employee resides.

          street_address1: Primary street address of the employee.

          zip: ZIP code for the employee's residence.

          middle_name: Middle name of the employee.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/employee",
            body=maybe_transform(
                {
                    "city": city,
                    "dob": dob,
                    "email": email,
                    "employee_id": employee_id,
                    "employer_id": employer_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "org_id": org_id,
                    "phone": phone,
                    "ssn": ssn,
                    "state": state,
                    "street_address1": street_address1,
                    "zip": zip,
                    "middle_name": middle_name,
                },
                employee_create_params.EmployeeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeCreateResponse,
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
    ) -> Employee:
        """
        Retrieve employee information based on the specified ID type and ID.

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
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            f"/employee/{id_type}/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employee,
        )

    def update(
        self,
        id: str,
        *,
        id_type: str,
        city: str | NotGiven = NOT_GIVEN,
        debit_id: str | NotGiven = NOT_GIVEN,
        dob: Union[str, date] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        employee_id: str | NotGiven = NOT_GIVEN,
        employer_id: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        org_id: int | NotGiven = NOT_GIVEN,
        owner: bool | NotGiven = NOT_GIVEN,
        passport_account_id: str | NotGiven = NOT_GIVEN,
        passport_customer_id: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        ssn: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        street_address1: str | NotGiven = NOT_GIVEN,
        zip: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployeeUpdateResponse:
        """
        Update employee information based on the specified ID type and ID.

        Args:
          city: City where the employee resides.

          debit_id: Unique identifier for the debit card.

          dob: Date of birth of the employee.

          email: Email address of the employee.

          employee_id: Unique identifier for the employee in the system. Can be used as external
              identifier.

          employer_id: Identifier for the employer associated with the employee. Can be used as
              external identifier. If provided, must match an existing employer's employerId.

          first_name: First name of the employee.

          last_name: Last name of the employee.

          org_id: Organization identifier associated with the employee.

          owner: Flag indicating if the employee is an owner.

          passport_account_id: Account ID for passport processing.

          passport_customer_id: Customer ID for passport processing.

          phone: Contact phone number for the employee.

          ssn: Social Security Number (SSN) of the employee.

          state: State where the employee resides.

          status: Current employment status of the employee.

          street_address1: Primary street address of the employee.

          zip: ZIP code for the employee's residence.

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
            f"/employee/{id_type}/{id}",
            body=maybe_transform(
                {
                    "city": city,
                    "debit_id": debit_id,
                    "dob": dob,
                    "email": email,
                    "employee_id": employee_id,
                    "employer_id": employer_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "org_id": org_id,
                    "owner": owner,
                    "passport_account_id": passport_account_id,
                    "passport_customer_id": passport_customer_id,
                    "phone": phone,
                    "ssn": ssn,
                    "state": state,
                    "status": status,
                    "street_address1": street_address1,
                    "zip": zip,
                },
                employee_update_params.EmployeeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeUpdateResponse,
        )

    def archive(
        self,
        id: str,
        *,
        id_type: str,
        admin_memo: str | NotGiven = NOT_GIVEN,
        archived_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        archived_reason: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployeeArchiveResponse:
        """Archive an employee based on the specified ID type and ID.

        This action also
        queues a balance update to zero.

        Args:
          admin_memo: A message attached to the archive.

          archived_at: The date for the archive to take place.

          archived_reason: The reason for the archive.

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
            f"/employee/{id_type}/{id}/archive",
            body=maybe_transform(
                {
                    "admin_memo": admin_memo,
                    "archived_at": archived_at,
                    "archived_reason": archived_reason,
                },
                employee_archive_params.EmployeeArchiveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeArchiveResponse,
        )

    def batch_create(
        self,
        *,
        body: Iterable[EmployeeCoreParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployeeBatchCreateResponse:
        """
        Submits employee basic information in a list and returns the complete employee
        records.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/employee/batch",
            body=maybe_transform(body, Iterable[EmployeeCoreParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeBatchCreateResponse,
        )

    def get_payment_methods(
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
    ) -> EmployeeGetPaymentMethodsResponse:
        """
        Retrieve the bank and debit card information of an employee based on the
        specified ID type and ID.

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
            f"/employee/{id_type}/{id}/payment-methods",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeGetPaymentMethodsResponse,
        )

    def get_transactions(
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
    ) -> EmployeeGetTransactionsResponse:
        """
        Retrieve the list of transactions for an employee based on the specified ID type
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
            f"/employee/{id_type}/{id}/transaction",
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
                    employee_get_transactions_params.EmployeeGetTransactionsParams,
                ),
            ),
            cast_to=EmployeeGetTransactionsResponse,
        )

    def unarchive(
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
    ) -> EmployeeUnarchiveResponse:
        """
        Unarchive an employee based on the specified ID type and ID.

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
        return self._post(
            f"/employee/{id_type}/{id}/unarchive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeUnarchiveResponse,
        )


class AsyncEmployeeResource(AsyncAPIResource):
    @cached_property
    def balance(self) -> AsyncBalanceResource:
        return AsyncBalanceResource(self._client)

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

    async def create(
        self,
        *,
        city: str,
        dob: Union[str, date],
        email: str,
        employee_id: str,
        employer_id: str,
        first_name: str,
        last_name: str,
        org_id: int,
        phone: str,
        ssn: str,
        state: str,
        street_address1: str,
        zip: str,
        middle_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployeeCreateResponse:
        """
        Submits employee basic information and returns the complete employee record.

        Args:
          city: City where the employee resides.

          dob: Date of birth of the employee.

          email: Email address of the employee.

          employee_id: Unique identifier for the employee in the system. Can be used as external
              identifier.

          employer_id: Identifier for the employer associated with the employee. Can be used as
              external identifier. If provided, must match an existing employer's employerId.

          first_name: First name of the employee.

          last_name: Last name of the employee.

          org_id: Organization identifier associated with the employee.

          phone: Contact phone number for the employee.

          ssn: Social Security Number (SSN) of the employee.

          state: State where the employee resides.

          street_address1: Primary street address of the employee.

          zip: ZIP code for the employee's residence.

          middle_name: Middle name of the employee.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/employee",
            body=await async_maybe_transform(
                {
                    "city": city,
                    "dob": dob,
                    "email": email,
                    "employee_id": employee_id,
                    "employer_id": employer_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "org_id": org_id,
                    "phone": phone,
                    "ssn": ssn,
                    "state": state,
                    "street_address1": street_address1,
                    "zip": zip,
                    "middle_name": middle_name,
                },
                employee_create_params.EmployeeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeCreateResponse,
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
    ) -> Employee:
        """
        Retrieve employee information based on the specified ID type and ID.

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
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            f"/employee/{id_type}/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employee,
        )

    async def update(
        self,
        id: str,
        *,
        id_type: str,
        city: str | NotGiven = NOT_GIVEN,
        debit_id: str | NotGiven = NOT_GIVEN,
        dob: Union[str, date] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        employee_id: str | NotGiven = NOT_GIVEN,
        employer_id: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        org_id: int | NotGiven = NOT_GIVEN,
        owner: bool | NotGiven = NOT_GIVEN,
        passport_account_id: str | NotGiven = NOT_GIVEN,
        passport_customer_id: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        ssn: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        street_address1: str | NotGiven = NOT_GIVEN,
        zip: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployeeUpdateResponse:
        """
        Update employee information based on the specified ID type and ID.

        Args:
          city: City where the employee resides.

          debit_id: Unique identifier for the debit card.

          dob: Date of birth of the employee.

          email: Email address of the employee.

          employee_id: Unique identifier for the employee in the system. Can be used as external
              identifier.

          employer_id: Identifier for the employer associated with the employee. Can be used as
              external identifier. If provided, must match an existing employer's employerId.

          first_name: First name of the employee.

          last_name: Last name of the employee.

          org_id: Organization identifier associated with the employee.

          owner: Flag indicating if the employee is an owner.

          passport_account_id: Account ID for passport processing.

          passport_customer_id: Customer ID for passport processing.

          phone: Contact phone number for the employee.

          ssn: Social Security Number (SSN) of the employee.

          state: State where the employee resides.

          status: Current employment status of the employee.

          street_address1: Primary street address of the employee.

          zip: ZIP code for the employee's residence.

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
            f"/employee/{id_type}/{id}",
            body=await async_maybe_transform(
                {
                    "city": city,
                    "debit_id": debit_id,
                    "dob": dob,
                    "email": email,
                    "employee_id": employee_id,
                    "employer_id": employer_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "org_id": org_id,
                    "owner": owner,
                    "passport_account_id": passport_account_id,
                    "passport_customer_id": passport_customer_id,
                    "phone": phone,
                    "ssn": ssn,
                    "state": state,
                    "status": status,
                    "street_address1": street_address1,
                    "zip": zip,
                },
                employee_update_params.EmployeeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeUpdateResponse,
        )

    async def archive(
        self,
        id: str,
        *,
        id_type: str,
        admin_memo: str | NotGiven = NOT_GIVEN,
        archived_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        archived_reason: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployeeArchiveResponse:
        """Archive an employee based on the specified ID type and ID.

        This action also
        queues a balance update to zero.

        Args:
          admin_memo: A message attached to the archive.

          archived_at: The date for the archive to take place.

          archived_reason: The reason for the archive.

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
            f"/employee/{id_type}/{id}/archive",
            body=await async_maybe_transform(
                {
                    "admin_memo": admin_memo,
                    "archived_at": archived_at,
                    "archived_reason": archived_reason,
                },
                employee_archive_params.EmployeeArchiveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeArchiveResponse,
        )

    async def batch_create(
        self,
        *,
        body: Iterable[EmployeeCoreParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployeeBatchCreateResponse:
        """
        Submits employee basic information in a list and returns the complete employee
        records.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/employee/batch",
            body=await async_maybe_transform(body, Iterable[EmployeeCoreParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeBatchCreateResponse,
        )

    async def get_payment_methods(
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
    ) -> EmployeeGetPaymentMethodsResponse:
        """
        Retrieve the bank and debit card information of an employee based on the
        specified ID type and ID.

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
            f"/employee/{id_type}/{id}/payment-methods",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeGetPaymentMethodsResponse,
        )

    async def get_transactions(
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
    ) -> EmployeeGetTransactionsResponse:
        """
        Retrieve the list of transactions for an employee based on the specified ID type
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
            f"/employee/{id_type}/{id}/transaction",
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
                    employee_get_transactions_params.EmployeeGetTransactionsParams,
                ),
            ),
            cast_to=EmployeeGetTransactionsResponse,
        )

    async def unarchive(
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
    ) -> EmployeeUnarchiveResponse:
        """
        Unarchive an employee based on the specified ID type and ID.

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
        return await self._post(
            f"/employee/{id_type}/{id}/unarchive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeUnarchiveResponse,
        )


class EmployeeResourceWithRawResponse:
    def __init__(self, employee: EmployeeResource) -> None:
        self._employee = employee

        self.create = to_raw_response_wrapper(
            employee.create,
        )
        self.retrieve = to_raw_response_wrapper(
            employee.retrieve,
        )
        self.update = to_raw_response_wrapper(
            employee.update,
        )
        self.archive = to_raw_response_wrapper(
            employee.archive,
        )
        self.batch_create = to_raw_response_wrapper(
            employee.batch_create,
        )
        self.get_payment_methods = to_raw_response_wrapper(
            employee.get_payment_methods,
        )
        self.get_transactions = to_raw_response_wrapper(
            employee.get_transactions,
        )
        self.unarchive = to_raw_response_wrapper(
            employee.unarchive,
        )

    @cached_property
    def balance(self) -> BalanceResourceWithRawResponse:
        return BalanceResourceWithRawResponse(self._employee.balance)


class AsyncEmployeeResourceWithRawResponse:
    def __init__(self, employee: AsyncEmployeeResource) -> None:
        self._employee = employee

        self.create = async_to_raw_response_wrapper(
            employee.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            employee.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            employee.update,
        )
        self.archive = async_to_raw_response_wrapper(
            employee.archive,
        )
        self.batch_create = async_to_raw_response_wrapper(
            employee.batch_create,
        )
        self.get_payment_methods = async_to_raw_response_wrapper(
            employee.get_payment_methods,
        )
        self.get_transactions = async_to_raw_response_wrapper(
            employee.get_transactions,
        )
        self.unarchive = async_to_raw_response_wrapper(
            employee.unarchive,
        )

    @cached_property
    def balance(self) -> AsyncBalanceResourceWithRawResponse:
        return AsyncBalanceResourceWithRawResponse(self._employee.balance)


class EmployeeResourceWithStreamingResponse:
    def __init__(self, employee: EmployeeResource) -> None:
        self._employee = employee

        self.create = to_streamed_response_wrapper(
            employee.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            employee.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            employee.update,
        )
        self.archive = to_streamed_response_wrapper(
            employee.archive,
        )
        self.batch_create = to_streamed_response_wrapper(
            employee.batch_create,
        )
        self.get_payment_methods = to_streamed_response_wrapper(
            employee.get_payment_methods,
        )
        self.get_transactions = to_streamed_response_wrapper(
            employee.get_transactions,
        )
        self.unarchive = to_streamed_response_wrapper(
            employee.unarchive,
        )

    @cached_property
    def balance(self) -> BalanceResourceWithStreamingResponse:
        return BalanceResourceWithStreamingResponse(self._employee.balance)


class AsyncEmployeeResourceWithStreamingResponse:
    def __init__(self, employee: AsyncEmployeeResource) -> None:
        self._employee = employee

        self.create = async_to_streamed_response_wrapper(
            employee.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            employee.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            employee.update,
        )
        self.archive = async_to_streamed_response_wrapper(
            employee.archive,
        )
        self.batch_create = async_to_streamed_response_wrapper(
            employee.batch_create,
        )
        self.get_payment_methods = async_to_streamed_response_wrapper(
            employee.get_payment_methods,
        )
        self.get_transactions = async_to_streamed_response_wrapper(
            employee.get_transactions,
        )
        self.unarchive = async_to_streamed_response_wrapper(
            employee.unarchive,
        )

    @cached_property
    def balance(self) -> AsyncBalanceResourceWithStreamingResponse:
        return AsyncBalanceResourceWithStreamingResponse(self._employee.balance)
