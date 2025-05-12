# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    report_retrieve_payments_report_params,
    report_retrieve_archived_accounts_report_params,
    report_retrieve_funding_transfer_detail_report_params,
    report_retrieve_nonzero_balance_accounts_report_params,
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
from ..types.report_retrieve_payments_report_response import ReportRetrievePaymentsReportResponse
from ..types.report_retrieve_archived_accounts_report_response import ReportRetrieveArchivedAccountsReportResponse
from ..types.report_retrieve_funding_transfer_detail_report_response import (
    ReportRetrieveFundingTransferDetailReportResponse,
)
from ..types.report_retrieve_nonzero_balance_accounts_report_response import (
    ReportRetrieveNonzeroBalanceAccountsReportResponse,
)

__all__ = ["ReportResource", "AsyncReportResource"]


class ReportResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felippemr/ambient-sdk#accessing-raw-response-data-eg-headers
        """
        return ReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felippemr/ambient-sdk#with_streaming_response
        """
        return ReportResourceWithStreamingResponse(self)

    def retrieve_archived_accounts_report(
        self,
        *,
        employer_id: str | NotGiven = NOT_GIVEN,
        end_date: str | NotGiven = NOT_GIVEN,
        start_date: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReportRetrieveArchivedAccountsReportResponse:
        """
        Retrieve a report of archived accounts, including optional filters for a list of
        employer IDs and a time period.

        Args:
          employer_id: A comma-separated list of employer IDs to filter the archived accounts.

          end_date: The end date for filtering employees (e.g., "03-25-2024").

          start_date: The start date for filtering employees (e.g., "03-20-2024").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/report/archived",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "employer_id": employer_id,
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    report_retrieve_archived_accounts_report_params.ReportRetrieveArchivedAccountsReportParams,
                ),
            ),
            cast_to=ReportRetrieveArchivedAccountsReportResponse,
        )

    def retrieve_funding_transfer_detail_report(
        self,
        *,
        employer_id: str | NotGiven = NOT_GIVEN,
        end_date: str | NotGiven = NOT_GIVEN,
        start_date: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReportRetrieveFundingTransferDetailReportResponse:
        """
        Retrieve a report of funding transfers, including optional filters for a list of
        employer IDs and a date range.

        Args:
          employer_id: A comma-separated list of employer IDs to filter the funding transfers.

          end_date: The end date for filtering transactions (e.g., "03-25-2024").

          start_date: The start date for filtering transactions (e.g., "03-20-2024").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/report/funding",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "employer_id": employer_id,
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    report_retrieve_funding_transfer_detail_report_params.ReportRetrieveFundingTransferDetailReportParams,
                ),
            ),
            cast_to=ReportRetrieveFundingTransferDetailReportResponse,
        )

    def retrieve_nonzero_balance_accounts_report(
        self,
        *,
        employer_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReportRetrieveNonzeroBalanceAccountsReportResponse:
        """
        Retrieve a report of accounts that have a non-zero balance, including optional
        filters for a list of employer IDs.

        Args:
          employer_id: A comma-separated list of employer IDs to filter the accounts with non-zero
              balance.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/report/nonzero",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"employer_id": employer_id},
                    report_retrieve_nonzero_balance_accounts_report_params.ReportRetrieveNonzeroBalanceAccountsReportParams,
                ),
            ),
            cast_to=ReportRetrieveNonzeroBalanceAccountsReportResponse,
        )

    def retrieve_payments_report(
        self,
        *,
        employer_id: str | NotGiven = NOT_GIVEN,
        end_date: str | NotGiven = NOT_GIVEN,
        start_date: str | NotGiven = NOT_GIVEN,
        type_text: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReportRetrievePaymentsReportResponse:
        """
        Retrieve a report of payment transactions, including optional filters for date
        range and transaction type.

        Args:
          employer_id: A comma-separated list of employer IDs to filter the transactions.

          end_date: The end date for filtering transactions (e.g., "03-25-2024").

          start_date: The start date for filtering transactions (e.g., "03-20-2024").

          type_text: The type of transactions to filter (e.g., "card" or "ach").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/report/payments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "employer_id": employer_id,
                        "end_date": end_date,
                        "start_date": start_date,
                        "type_text": type_text,
                    },
                    report_retrieve_payments_report_params.ReportRetrievePaymentsReportParams,
                ),
            ),
            cast_to=ReportRetrievePaymentsReportResponse,
        )


class AsyncReportResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/felippemr/ambient-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/felippemr/ambient-sdk#with_streaming_response
        """
        return AsyncReportResourceWithStreamingResponse(self)

    async def retrieve_archived_accounts_report(
        self,
        *,
        employer_id: str | NotGiven = NOT_GIVEN,
        end_date: str | NotGiven = NOT_GIVEN,
        start_date: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReportRetrieveArchivedAccountsReportResponse:
        """
        Retrieve a report of archived accounts, including optional filters for a list of
        employer IDs and a time period.

        Args:
          employer_id: A comma-separated list of employer IDs to filter the archived accounts.

          end_date: The end date for filtering employees (e.g., "03-25-2024").

          start_date: The start date for filtering employees (e.g., "03-20-2024").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/report/archived",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "employer_id": employer_id,
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    report_retrieve_archived_accounts_report_params.ReportRetrieveArchivedAccountsReportParams,
                ),
            ),
            cast_to=ReportRetrieveArchivedAccountsReportResponse,
        )

    async def retrieve_funding_transfer_detail_report(
        self,
        *,
        employer_id: str | NotGiven = NOT_GIVEN,
        end_date: str | NotGiven = NOT_GIVEN,
        start_date: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReportRetrieveFundingTransferDetailReportResponse:
        """
        Retrieve a report of funding transfers, including optional filters for a list of
        employer IDs and a date range.

        Args:
          employer_id: A comma-separated list of employer IDs to filter the funding transfers.

          end_date: The end date for filtering transactions (e.g., "03-25-2024").

          start_date: The start date for filtering transactions (e.g., "03-20-2024").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/report/funding",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "employer_id": employer_id,
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    report_retrieve_funding_transfer_detail_report_params.ReportRetrieveFundingTransferDetailReportParams,
                ),
            ),
            cast_to=ReportRetrieveFundingTransferDetailReportResponse,
        )

    async def retrieve_nonzero_balance_accounts_report(
        self,
        *,
        employer_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReportRetrieveNonzeroBalanceAccountsReportResponse:
        """
        Retrieve a report of accounts that have a non-zero balance, including optional
        filters for a list of employer IDs.

        Args:
          employer_id: A comma-separated list of employer IDs to filter the accounts with non-zero
              balance.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/report/nonzero",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"employer_id": employer_id},
                    report_retrieve_nonzero_balance_accounts_report_params.ReportRetrieveNonzeroBalanceAccountsReportParams,
                ),
            ),
            cast_to=ReportRetrieveNonzeroBalanceAccountsReportResponse,
        )

    async def retrieve_payments_report(
        self,
        *,
        employer_id: str | NotGiven = NOT_GIVEN,
        end_date: str | NotGiven = NOT_GIVEN,
        start_date: str | NotGiven = NOT_GIVEN,
        type_text: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReportRetrievePaymentsReportResponse:
        """
        Retrieve a report of payment transactions, including optional filters for date
        range and transaction type.

        Args:
          employer_id: A comma-separated list of employer IDs to filter the transactions.

          end_date: The end date for filtering transactions (e.g., "03-25-2024").

          start_date: The start date for filtering transactions (e.g., "03-20-2024").

          type_text: The type of transactions to filter (e.g., "card" or "ach").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/report/payments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "employer_id": employer_id,
                        "end_date": end_date,
                        "start_date": start_date,
                        "type_text": type_text,
                    },
                    report_retrieve_payments_report_params.ReportRetrievePaymentsReportParams,
                ),
            ),
            cast_to=ReportRetrievePaymentsReportResponse,
        )


class ReportResourceWithRawResponse:
    def __init__(self, report: ReportResource) -> None:
        self._report = report

        self.retrieve_archived_accounts_report = to_raw_response_wrapper(
            report.retrieve_archived_accounts_report,
        )
        self.retrieve_funding_transfer_detail_report = to_raw_response_wrapper(
            report.retrieve_funding_transfer_detail_report,
        )
        self.retrieve_nonzero_balance_accounts_report = to_raw_response_wrapper(
            report.retrieve_nonzero_balance_accounts_report,
        )
        self.retrieve_payments_report = to_raw_response_wrapper(
            report.retrieve_payments_report,
        )


class AsyncReportResourceWithRawResponse:
    def __init__(self, report: AsyncReportResource) -> None:
        self._report = report

        self.retrieve_archived_accounts_report = async_to_raw_response_wrapper(
            report.retrieve_archived_accounts_report,
        )
        self.retrieve_funding_transfer_detail_report = async_to_raw_response_wrapper(
            report.retrieve_funding_transfer_detail_report,
        )
        self.retrieve_nonzero_balance_accounts_report = async_to_raw_response_wrapper(
            report.retrieve_nonzero_balance_accounts_report,
        )
        self.retrieve_payments_report = async_to_raw_response_wrapper(
            report.retrieve_payments_report,
        )


class ReportResourceWithStreamingResponse:
    def __init__(self, report: ReportResource) -> None:
        self._report = report

        self.retrieve_archived_accounts_report = to_streamed_response_wrapper(
            report.retrieve_archived_accounts_report,
        )
        self.retrieve_funding_transfer_detail_report = to_streamed_response_wrapper(
            report.retrieve_funding_transfer_detail_report,
        )
        self.retrieve_nonzero_balance_accounts_report = to_streamed_response_wrapper(
            report.retrieve_nonzero_balance_accounts_report,
        )
        self.retrieve_payments_report = to_streamed_response_wrapper(
            report.retrieve_payments_report,
        )


class AsyncReportResourceWithStreamingResponse:
    def __init__(self, report: AsyncReportResource) -> None:
        self._report = report

        self.retrieve_archived_accounts_report = async_to_streamed_response_wrapper(
            report.retrieve_archived_accounts_report,
        )
        self.retrieve_funding_transfer_detail_report = async_to_streamed_response_wrapper(
            report.retrieve_funding_transfer_detail_report,
        )
        self.retrieve_nonzero_balance_accounts_report = async_to_streamed_response_wrapper(
            report.retrieve_nonzero_balance_accounts_report,
        )
        self.retrieve_payments_report = async_to_streamed_response_wrapper(
            report.retrieve_payments_report,
        )
