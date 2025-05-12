# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ambient_sdk import AmbientSDK, AsyncAmbientSDK
from tests.utils import assert_matches_type
from ambient_sdk.types import (
    ReportRetrievePaymentsReportResponse,
    ReportRetrieveArchivedAccountsReportResponse,
    ReportRetrieveFundingTransferDetailReportResponse,
    ReportRetrieveNonzeroBalanceAccountsReportResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_archived_accounts_report(self, client: AmbientSDK) -> None:
        report = client.report.retrieve_archived_accounts_report()
        assert_matches_type(ReportRetrieveArchivedAccountsReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_archived_accounts_report_with_all_params(self, client: AmbientSDK) -> None:
        report = client.report.retrieve_archived_accounts_report(
            employer_id="employerId",
            end_date="endDate",
            start_date="startDate",
        )
        assert_matches_type(ReportRetrieveArchivedAccountsReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_archived_accounts_report(self, client: AmbientSDK) -> None:
        response = client.report.with_raw_response.retrieve_archived_accounts_report()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportRetrieveArchivedAccountsReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_archived_accounts_report(self, client: AmbientSDK) -> None:
        with client.report.with_streaming_response.retrieve_archived_accounts_report() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportRetrieveArchivedAccountsReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_funding_transfer_detail_report(self, client: AmbientSDK) -> None:
        report = client.report.retrieve_funding_transfer_detail_report()
        assert_matches_type(ReportRetrieveFundingTransferDetailReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_funding_transfer_detail_report_with_all_params(self, client: AmbientSDK) -> None:
        report = client.report.retrieve_funding_transfer_detail_report(
            employer_id="employerId",
            end_date="endDate",
            start_date="startDate",
        )
        assert_matches_type(ReportRetrieveFundingTransferDetailReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_funding_transfer_detail_report(self, client: AmbientSDK) -> None:
        response = client.report.with_raw_response.retrieve_funding_transfer_detail_report()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportRetrieveFundingTransferDetailReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_funding_transfer_detail_report(self, client: AmbientSDK) -> None:
        with client.report.with_streaming_response.retrieve_funding_transfer_detail_report() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportRetrieveFundingTransferDetailReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_nonzero_balance_accounts_report(self, client: AmbientSDK) -> None:
        report = client.report.retrieve_nonzero_balance_accounts_report()
        assert_matches_type(ReportRetrieveNonzeroBalanceAccountsReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_nonzero_balance_accounts_report_with_all_params(self, client: AmbientSDK) -> None:
        report = client.report.retrieve_nonzero_balance_accounts_report(
            employer_id="employerId",
        )
        assert_matches_type(ReportRetrieveNonzeroBalanceAccountsReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_nonzero_balance_accounts_report(self, client: AmbientSDK) -> None:
        response = client.report.with_raw_response.retrieve_nonzero_balance_accounts_report()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportRetrieveNonzeroBalanceAccountsReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_nonzero_balance_accounts_report(self, client: AmbientSDK) -> None:
        with client.report.with_streaming_response.retrieve_nonzero_balance_accounts_report() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportRetrieveNonzeroBalanceAccountsReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_payments_report(self, client: AmbientSDK) -> None:
        report = client.report.retrieve_payments_report()
        assert_matches_type(ReportRetrievePaymentsReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_payments_report_with_all_params(self, client: AmbientSDK) -> None:
        report = client.report.retrieve_payments_report(
            employer_id="employerId",
            end_date="endDate",
            start_date="startDate",
            type_text="typeText",
        )
        assert_matches_type(ReportRetrievePaymentsReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_payments_report(self, client: AmbientSDK) -> None:
        response = client.report.with_raw_response.retrieve_payments_report()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportRetrievePaymentsReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_payments_report(self, client: AmbientSDK) -> None:
        with client.report.with_streaming_response.retrieve_payments_report() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportRetrievePaymentsReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReport:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_archived_accounts_report(self, async_client: AsyncAmbientSDK) -> None:
        report = await async_client.report.retrieve_archived_accounts_report()
        assert_matches_type(ReportRetrieveArchivedAccountsReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_archived_accounts_report_with_all_params(
        self, async_client: AsyncAmbientSDK
    ) -> None:
        report = await async_client.report.retrieve_archived_accounts_report(
            employer_id="employerId",
            end_date="endDate",
            start_date="startDate",
        )
        assert_matches_type(ReportRetrieveArchivedAccountsReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_archived_accounts_report(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.report.with_raw_response.retrieve_archived_accounts_report()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportRetrieveArchivedAccountsReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_archived_accounts_report(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.report.with_streaming_response.retrieve_archived_accounts_report() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportRetrieveArchivedAccountsReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_funding_transfer_detail_report(self, async_client: AsyncAmbientSDK) -> None:
        report = await async_client.report.retrieve_funding_transfer_detail_report()
        assert_matches_type(ReportRetrieveFundingTransferDetailReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_funding_transfer_detail_report_with_all_params(
        self, async_client: AsyncAmbientSDK
    ) -> None:
        report = await async_client.report.retrieve_funding_transfer_detail_report(
            employer_id="employerId",
            end_date="endDate",
            start_date="startDate",
        )
        assert_matches_type(ReportRetrieveFundingTransferDetailReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_funding_transfer_detail_report(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.report.with_raw_response.retrieve_funding_transfer_detail_report()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportRetrieveFundingTransferDetailReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_funding_transfer_detail_report(
        self, async_client: AsyncAmbientSDK
    ) -> None:
        async with async_client.report.with_streaming_response.retrieve_funding_transfer_detail_report() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportRetrieveFundingTransferDetailReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_nonzero_balance_accounts_report(self, async_client: AsyncAmbientSDK) -> None:
        report = await async_client.report.retrieve_nonzero_balance_accounts_report()
        assert_matches_type(ReportRetrieveNonzeroBalanceAccountsReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_nonzero_balance_accounts_report_with_all_params(
        self, async_client: AsyncAmbientSDK
    ) -> None:
        report = await async_client.report.retrieve_nonzero_balance_accounts_report(
            employer_id="employerId",
        )
        assert_matches_type(ReportRetrieveNonzeroBalanceAccountsReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_nonzero_balance_accounts_report(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.report.with_raw_response.retrieve_nonzero_balance_accounts_report()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportRetrieveNonzeroBalanceAccountsReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_nonzero_balance_accounts_report(
        self, async_client: AsyncAmbientSDK
    ) -> None:
        async with async_client.report.with_streaming_response.retrieve_nonzero_balance_accounts_report() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportRetrieveNonzeroBalanceAccountsReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_payments_report(self, async_client: AsyncAmbientSDK) -> None:
        report = await async_client.report.retrieve_payments_report()
        assert_matches_type(ReportRetrievePaymentsReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_payments_report_with_all_params(self, async_client: AsyncAmbientSDK) -> None:
        report = await async_client.report.retrieve_payments_report(
            employer_id="employerId",
            end_date="endDate",
            start_date="startDate",
            type_text="typeText",
        )
        assert_matches_type(ReportRetrievePaymentsReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_payments_report(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.report.with_raw_response.retrieve_payments_report()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportRetrievePaymentsReportResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_payments_report(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.report.with_streaming_response.retrieve_payments_report() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportRetrievePaymentsReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True
