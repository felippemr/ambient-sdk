# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ambient_sdk import AmbientSDK, AsyncAmbientSDK
from tests.utils import assert_matches_type
from ambient_sdk.types import (
    EmployerCreateResponse,
    EmployerUpdateResponse,
    EmployerRetrieveResponse,
    EmployerCreateBatchResponse,
    EmployerRetrieveBalanceResponse,
    EmployerListTransactionsResponse,
    EmployerRetrieveBankInfoResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmployer:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: AmbientSDK) -> None:
        employer = client.employer.create(
            city="Arizona",
            ein="15-2852123",
            employer_id="172499",
            name="ACME Corporation",
            org_id=5,
            state="AZ",
            street_address1="123 Apple St",
            zip="55232",
        )
        assert_matches_type(EmployerCreateResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: AmbientSDK) -> None:
        employer = client.employer.create(
            city="Arizona",
            ein="15-2852123",
            employer_id="172499",
            name="ACME Corporation",
            org_id=5,
            state="AZ",
            street_address1="123 Apple St",
            zip="55232",
            street_address2="Apt 101",
        )
        assert_matches_type(EmployerCreateResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: AmbientSDK) -> None:
        response = client.employer.with_raw_response.create(
            city="Arizona",
            ein="15-2852123",
            employer_id="172499",
            name="ACME Corporation",
            org_id=5,
            state="AZ",
            street_address1="123 Apple St",
            zip="55232",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerCreateResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: AmbientSDK) -> None:
        with client.employer.with_streaming_response.create(
            city="Arizona",
            ein="15-2852123",
            employer_id="172499",
            name="ACME Corporation",
            org_id=5,
            state="AZ",
            street_address1="123 Apple St",
            zip="55232",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerCreateResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: AmbientSDK) -> None:
        employer = client.employer.retrieve(
            id="id",
            id_type="idType",
        )
        assert_matches_type(EmployerRetrieveResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: AmbientSDK) -> None:
        response = client.employer.with_raw_response.retrieve(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerRetrieveResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: AmbientSDK) -> None:
        with client.employer.with_streaming_response.retrieve(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerRetrieveResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: AmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            client.employer.with_raw_response.retrieve(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employer.with_raw_response.retrieve(
                id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: AmbientSDK) -> None:
        employer = client.employer.update(
            id="id",
            id_type="idType",
        )
        assert_matches_type(EmployerUpdateResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: AmbientSDK) -> None:
        employer = client.employer.update(
            id="id",
            id_type="idType",
            city="city",
            dba="dba",
            ein="ein",
            employer_id="employerId",
            name="name",
            org_id=0,
            passport_account_id="passportAccountId",
            passport_customer_id="passportCustomerId",
            state="state",
            street_address1="streetAddress1",
            street_address2="streetAddress2",
            zip="zip",
        )
        assert_matches_type(EmployerUpdateResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: AmbientSDK) -> None:
        response = client.employer.with_raw_response.update(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerUpdateResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: AmbientSDK) -> None:
        with client.employer.with_streaming_response.update(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerUpdateResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: AmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            client.employer.with_raw_response.update(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employer.with_raw_response.update(
                id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_batch(self, client: AmbientSDK) -> None:
        employer = client.employer.create_batch(
            body=[
                {
                    "city": "Miami",
                    "ein": "11-2223333",
                    "employer_id": "21454",
                    "name": "Company 1",
                    "org_id": 5,
                    "state": "FL",
                    "street_address1": "11 Main St",
                    "zip": "35918",
                },
                {
                    "city": "Miami",
                    "ein": "11-2224444",
                    "employer_id": "83291",
                    "name": "Company 2",
                    "org_id": 5,
                    "state": "FL",
                    "street_address1": "12 Main St",
                    "zip": "35918",
                },
            ],
        )
        assert_matches_type(EmployerCreateBatchResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_batch(self, client: AmbientSDK) -> None:
        response = client.employer.with_raw_response.create_batch(
            body=[
                {
                    "city": "Miami",
                    "ein": "11-2223333",
                    "employer_id": "21454",
                    "name": "Company 1",
                    "org_id": 5,
                    "state": "FL",
                    "street_address1": "11 Main St",
                    "zip": "35918",
                },
                {
                    "city": "Miami",
                    "ein": "11-2224444",
                    "employer_id": "83291",
                    "name": "Company 2",
                    "org_id": 5,
                    "state": "FL",
                    "street_address1": "12 Main St",
                    "zip": "35918",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerCreateBatchResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_batch(self, client: AmbientSDK) -> None:
        with client.employer.with_streaming_response.create_batch(
            body=[
                {
                    "city": "Miami",
                    "ein": "11-2223333",
                    "employer_id": "21454",
                    "name": "Company 1",
                    "org_id": 5,
                    "state": "FL",
                    "street_address1": "11 Main St",
                    "zip": "35918",
                },
                {
                    "city": "Miami",
                    "ein": "11-2224444",
                    "employer_id": "83291",
                    "name": "Company 2",
                    "org_id": 5,
                    "state": "FL",
                    "street_address1": "12 Main St",
                    "zip": "35918",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerCreateBatchResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_transactions(self, client: AmbientSDK) -> None:
        employer = client.employer.list_transactions(
            id="id",
            id_type="idType",
            end_date="endDate",
            start_date="startDate",
        )
        assert_matches_type(EmployerListTransactionsResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_transactions(self, client: AmbientSDK) -> None:
        response = client.employer.with_raw_response.list_transactions(
            id="id",
            id_type="idType",
            end_date="endDate",
            start_date="startDate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerListTransactionsResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_transactions(self, client: AmbientSDK) -> None:
        with client.employer.with_streaming_response.list_transactions(
            id="id",
            id_type="idType",
            end_date="endDate",
            start_date="startDate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerListTransactionsResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_transactions(self, client: AmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            client.employer.with_raw_response.list_transactions(
                id="id",
                id_type="",
                end_date="endDate",
                start_date="startDate",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employer.with_raw_response.list_transactions(
                id="",
                id_type="idType",
                end_date="endDate",
                start_date="startDate",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_balance(self, client: AmbientSDK) -> None:
        employer = client.employer.retrieve_balance(
            id="id",
            id_type="idType",
        )
        assert_matches_type(EmployerRetrieveBalanceResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_balance(self, client: AmbientSDK) -> None:
        response = client.employer.with_raw_response.retrieve_balance(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerRetrieveBalanceResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_balance(self, client: AmbientSDK) -> None:
        with client.employer.with_streaming_response.retrieve_balance(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerRetrieveBalanceResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_balance(self, client: AmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            client.employer.with_raw_response.retrieve_balance(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employer.with_raw_response.retrieve_balance(
                id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_bank_info(self, client: AmbientSDK) -> None:
        employer = client.employer.retrieve_bank_info(
            id="id",
            id_type="idType",
        )
        assert_matches_type(EmployerRetrieveBankInfoResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_bank_info(self, client: AmbientSDK) -> None:
        response = client.employer.with_raw_response.retrieve_bank_info(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerRetrieveBankInfoResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_bank_info(self, client: AmbientSDK) -> None:
        with client.employer.with_streaming_response.retrieve_bank_info(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerRetrieveBankInfoResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_bank_info(self, client: AmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            client.employer.with_raw_response.retrieve_bank_info(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employer.with_raw_response.retrieve_bank_info(
                id="",
                id_type="idType",
            )


class TestAsyncEmployer:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncAmbientSDK) -> None:
        employer = await async_client.employer.create(
            city="Arizona",
            ein="15-2852123",
            employer_id="172499",
            name="ACME Corporation",
            org_id=5,
            state="AZ",
            street_address1="123 Apple St",
            zip="55232",
        )
        assert_matches_type(EmployerCreateResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAmbientSDK) -> None:
        employer = await async_client.employer.create(
            city="Arizona",
            ein="15-2852123",
            employer_id="172499",
            name="ACME Corporation",
            org_id=5,
            state="AZ",
            street_address1="123 Apple St",
            zip="55232",
            street_address2="Apt 101",
        )
        assert_matches_type(EmployerCreateResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.employer.with_raw_response.create(
            city="Arizona",
            ein="15-2852123",
            employer_id="172499",
            name="ACME Corporation",
            org_id=5,
            state="AZ",
            street_address1="123 Apple St",
            zip="55232",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerCreateResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.employer.with_streaming_response.create(
            city="Arizona",
            ein="15-2852123",
            employer_id="172499",
            name="ACME Corporation",
            org_id=5,
            state="AZ",
            street_address1="123 Apple St",
            zip="55232",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerCreateResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        employer = await async_client.employer.retrieve(
            id="id",
            id_type="idType",
        )
        assert_matches_type(EmployerRetrieveResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.employer.with_raw_response.retrieve(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerRetrieveResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.employer.with_streaming_response.retrieve(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerRetrieveResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            await async_client.employer.with_raw_response.retrieve(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employer.with_raw_response.retrieve(
                id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncAmbientSDK) -> None:
        employer = await async_client.employer.update(
            id="id",
            id_type="idType",
        )
        assert_matches_type(EmployerUpdateResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAmbientSDK) -> None:
        employer = await async_client.employer.update(
            id="id",
            id_type="idType",
            city="city",
            dba="dba",
            ein="ein",
            employer_id="employerId",
            name="name",
            org_id=0,
            passport_account_id="passportAccountId",
            passport_customer_id="passportCustomerId",
            state="state",
            street_address1="streetAddress1",
            street_address2="streetAddress2",
            zip="zip",
        )
        assert_matches_type(EmployerUpdateResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.employer.with_raw_response.update(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerUpdateResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.employer.with_streaming_response.update(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerUpdateResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncAmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            await async_client.employer.with_raw_response.update(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employer.with_raw_response.update(
                id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_batch(self, async_client: AsyncAmbientSDK) -> None:
        employer = await async_client.employer.create_batch(
            body=[
                {
                    "city": "Miami",
                    "ein": "11-2223333",
                    "employer_id": "21454",
                    "name": "Company 1",
                    "org_id": 5,
                    "state": "FL",
                    "street_address1": "11 Main St",
                    "zip": "35918",
                },
                {
                    "city": "Miami",
                    "ein": "11-2224444",
                    "employer_id": "83291",
                    "name": "Company 2",
                    "org_id": 5,
                    "state": "FL",
                    "street_address1": "12 Main St",
                    "zip": "35918",
                },
            ],
        )
        assert_matches_type(EmployerCreateBatchResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_batch(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.employer.with_raw_response.create_batch(
            body=[
                {
                    "city": "Miami",
                    "ein": "11-2223333",
                    "employer_id": "21454",
                    "name": "Company 1",
                    "org_id": 5,
                    "state": "FL",
                    "street_address1": "11 Main St",
                    "zip": "35918",
                },
                {
                    "city": "Miami",
                    "ein": "11-2224444",
                    "employer_id": "83291",
                    "name": "Company 2",
                    "org_id": 5,
                    "state": "FL",
                    "street_address1": "12 Main St",
                    "zip": "35918",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerCreateBatchResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_batch(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.employer.with_streaming_response.create_batch(
            body=[
                {
                    "city": "Miami",
                    "ein": "11-2223333",
                    "employer_id": "21454",
                    "name": "Company 1",
                    "org_id": 5,
                    "state": "FL",
                    "street_address1": "11 Main St",
                    "zip": "35918",
                },
                {
                    "city": "Miami",
                    "ein": "11-2224444",
                    "employer_id": "83291",
                    "name": "Company 2",
                    "org_id": 5,
                    "state": "FL",
                    "street_address1": "12 Main St",
                    "zip": "35918",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerCreateBatchResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_transactions(self, async_client: AsyncAmbientSDK) -> None:
        employer = await async_client.employer.list_transactions(
            id="id",
            id_type="idType",
            end_date="endDate",
            start_date="startDate",
        )
        assert_matches_type(EmployerListTransactionsResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_transactions(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.employer.with_raw_response.list_transactions(
            id="id",
            id_type="idType",
            end_date="endDate",
            start_date="startDate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerListTransactionsResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_transactions(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.employer.with_streaming_response.list_transactions(
            id="id",
            id_type="idType",
            end_date="endDate",
            start_date="startDate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerListTransactionsResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_transactions(self, async_client: AsyncAmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            await async_client.employer.with_raw_response.list_transactions(
                id="id",
                id_type="",
                end_date="endDate",
                start_date="startDate",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employer.with_raw_response.list_transactions(
                id="",
                id_type="idType",
                end_date="endDate",
                start_date="startDate",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_balance(self, async_client: AsyncAmbientSDK) -> None:
        employer = await async_client.employer.retrieve_balance(
            id="id",
            id_type="idType",
        )
        assert_matches_type(EmployerRetrieveBalanceResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_balance(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.employer.with_raw_response.retrieve_balance(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerRetrieveBalanceResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_balance(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.employer.with_streaming_response.retrieve_balance(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerRetrieveBalanceResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_balance(self, async_client: AsyncAmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            await async_client.employer.with_raw_response.retrieve_balance(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employer.with_raw_response.retrieve_balance(
                id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_bank_info(self, async_client: AsyncAmbientSDK) -> None:
        employer = await async_client.employer.retrieve_bank_info(
            id="id",
            id_type="idType",
        )
        assert_matches_type(EmployerRetrieveBankInfoResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_bank_info(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.employer.with_raw_response.retrieve_bank_info(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerRetrieveBankInfoResponse, employer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_bank_info(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.employer.with_streaming_response.retrieve_bank_info(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerRetrieveBankInfoResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_bank_info(self, async_client: AsyncAmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            await async_client.employer.with_raw_response.retrieve_bank_info(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employer.with_raw_response.retrieve_bank_info(
                id="",
                id_type="idType",
            )
