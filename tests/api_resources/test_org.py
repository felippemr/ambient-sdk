# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ambient_sdk import AmbientSDK, AsyncAmbientSDK
from tests.utils import assert_matches_type
from ambient_sdk.types import (
    OrgCreateResponse,
    OrgUpdateResponse,
    OrgRetrieveBalanceResponse,
    OrgListTransactionsResponse,
    OrgRetrieveBankInfoResponse,
)
from ambient_sdk.types.org import Org

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrg:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: AmbientSDK) -> None:
        org = client.org.create(
            city="New York",
            ein="14-8712553",
            name="Umbrella Org",
            state="NY",
            street_address1="123 Main St",
            zip="10021",
        )
        assert_matches_type(OrgCreateResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: AmbientSDK) -> None:
        org = client.org.create(
            city="New York",
            ein="14-8712553",
            name="Umbrella Org",
            state="NY",
            street_address1="123 Main St",
            zip="10021",
            parent=4,
            street_address2="Apt 5",
        )
        assert_matches_type(OrgCreateResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: AmbientSDK) -> None:
        response = client.org.with_raw_response.create(
            city="New York",
            ein="14-8712553",
            name="Umbrella Org",
            state="NY",
            street_address1="123 Main St",
            zip="10021",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgCreateResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: AmbientSDK) -> None:
        with client.org.with_streaming_response.create(
            city="New York",
            ein="14-8712553",
            name="Umbrella Org",
            state="NY",
            street_address1="123 Main St",
            zip="10021",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(OrgCreateResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: AmbientSDK) -> None:
        org = client.org.retrieve(
            id="id",
            id_type="idType",
        )
        assert_matches_type(Org, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: AmbientSDK) -> None:
        response = client.org.with_raw_response.retrieve(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(Org, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: AmbientSDK) -> None:
        with client.org.with_streaming_response.retrieve(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(Org, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: AmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            client.org.with_raw_response.retrieve(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.org.with_raw_response.retrieve(
                id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: AmbientSDK) -> None:
        org = client.org.update(
            path_id="id",
            id_type="idType",
        )
        assert_matches_type(OrgUpdateResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: AmbientSDK) -> None:
        org = client.org.update(
            path_id="id",
            id_type="idType",
            body_id=0,
            city="city",
            ein="ein",
            name="name",
            passport_account_id="passportAccountId",
            passport_customer_id="3330689",
            state="state",
            street_address1="streetAddress1",
            street_address2="streetAddress2",
            zip="zip",
        )
        assert_matches_type(OrgUpdateResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: AmbientSDK) -> None:
        response = client.org.with_raw_response.update(
            path_id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgUpdateResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: AmbientSDK) -> None:
        with client.org.with_streaming_response.update(
            path_id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(OrgUpdateResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: AmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            client.org.with_raw_response.update(
                path_id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.org.with_raw_response.update(
                path_id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_transactions(self, client: AmbientSDK) -> None:
        org = client.org.list_transactions(
            id="id",
            id_type="idType",
            end_date="endDate",
            start_date="startDate",
        )
        assert_matches_type(OrgListTransactionsResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_transactions_with_all_params(self, client: AmbientSDK) -> None:
        org = client.org.list_transactions(
            id="id",
            id_type="idType",
            end_date="endDate",
            start_date="startDate",
            limit=0,
            offset=0,
        )
        assert_matches_type(OrgListTransactionsResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_transactions(self, client: AmbientSDK) -> None:
        response = client.org.with_raw_response.list_transactions(
            id="id",
            id_type="idType",
            end_date="endDate",
            start_date="startDate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgListTransactionsResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_transactions(self, client: AmbientSDK) -> None:
        with client.org.with_streaming_response.list_transactions(
            id="id",
            id_type="idType",
            end_date="endDate",
            start_date="startDate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(OrgListTransactionsResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_transactions(self, client: AmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            client.org.with_raw_response.list_transactions(
                id="id",
                id_type="",
                end_date="endDate",
                start_date="startDate",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.org.with_raw_response.list_transactions(
                id="",
                id_type="idType",
                end_date="endDate",
                start_date="startDate",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_balance(self, client: AmbientSDK) -> None:
        org = client.org.retrieve_balance(
            id="id",
            id_type="idType",
        )
        assert_matches_type(OrgRetrieveBalanceResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_balance(self, client: AmbientSDK) -> None:
        response = client.org.with_raw_response.retrieve_balance(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgRetrieveBalanceResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_balance(self, client: AmbientSDK) -> None:
        with client.org.with_streaming_response.retrieve_balance(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(OrgRetrieveBalanceResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_balance(self, client: AmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            client.org.with_raw_response.retrieve_balance(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.org.with_raw_response.retrieve_balance(
                id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_bank_info(self, client: AmbientSDK) -> None:
        org = client.org.retrieve_bank_info(
            id="id",
            id_type="idType",
        )
        assert_matches_type(OrgRetrieveBankInfoResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_bank_info(self, client: AmbientSDK) -> None:
        response = client.org.with_raw_response.retrieve_bank_info(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgRetrieveBankInfoResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_bank_info(self, client: AmbientSDK) -> None:
        with client.org.with_streaming_response.retrieve_bank_info(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(OrgRetrieveBankInfoResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_bank_info(self, client: AmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            client.org.with_raw_response.retrieve_bank_info(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.org.with_raw_response.retrieve_bank_info(
                id="",
                id_type="idType",
            )


class TestAsyncOrg:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncAmbientSDK) -> None:
        org = await async_client.org.create(
            city="New York",
            ein="14-8712553",
            name="Umbrella Org",
            state="NY",
            street_address1="123 Main St",
            zip="10021",
        )
        assert_matches_type(OrgCreateResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAmbientSDK) -> None:
        org = await async_client.org.create(
            city="New York",
            ein="14-8712553",
            name="Umbrella Org",
            state="NY",
            street_address1="123 Main St",
            zip="10021",
            parent=4,
            street_address2="Apt 5",
        )
        assert_matches_type(OrgCreateResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.org.with_raw_response.create(
            city="New York",
            ein="14-8712553",
            name="Umbrella Org",
            state="NY",
            street_address1="123 Main St",
            zip="10021",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgCreateResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.org.with_streaming_response.create(
            city="New York",
            ein="14-8712553",
            name="Umbrella Org",
            state="NY",
            street_address1="123 Main St",
            zip="10021",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(OrgCreateResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        org = await async_client.org.retrieve(
            id="id",
            id_type="idType",
        )
        assert_matches_type(Org, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.org.with_raw_response.retrieve(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(Org, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.org.with_streaming_response.retrieve(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(Org, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            await async_client.org.with_raw_response.retrieve(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.org.with_raw_response.retrieve(
                id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncAmbientSDK) -> None:
        org = await async_client.org.update(
            path_id="id",
            id_type="idType",
        )
        assert_matches_type(OrgUpdateResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAmbientSDK) -> None:
        org = await async_client.org.update(
            path_id="id",
            id_type="idType",
            body_id=0,
            city="city",
            ein="ein",
            name="name",
            passport_account_id="passportAccountId",
            passport_customer_id="3330689",
            state="state",
            street_address1="streetAddress1",
            street_address2="streetAddress2",
            zip="zip",
        )
        assert_matches_type(OrgUpdateResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.org.with_raw_response.update(
            path_id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgUpdateResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.org.with_streaming_response.update(
            path_id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(OrgUpdateResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncAmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            await async_client.org.with_raw_response.update(
                path_id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.org.with_raw_response.update(
                path_id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_transactions(self, async_client: AsyncAmbientSDK) -> None:
        org = await async_client.org.list_transactions(
            id="id",
            id_type="idType",
            end_date="endDate",
            start_date="startDate",
        )
        assert_matches_type(OrgListTransactionsResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_transactions_with_all_params(self, async_client: AsyncAmbientSDK) -> None:
        org = await async_client.org.list_transactions(
            id="id",
            id_type="idType",
            end_date="endDate",
            start_date="startDate",
            limit=0,
            offset=0,
        )
        assert_matches_type(OrgListTransactionsResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_transactions(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.org.with_raw_response.list_transactions(
            id="id",
            id_type="idType",
            end_date="endDate",
            start_date="startDate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgListTransactionsResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_transactions(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.org.with_streaming_response.list_transactions(
            id="id",
            id_type="idType",
            end_date="endDate",
            start_date="startDate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(OrgListTransactionsResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_transactions(self, async_client: AsyncAmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            await async_client.org.with_raw_response.list_transactions(
                id="id",
                id_type="",
                end_date="endDate",
                start_date="startDate",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.org.with_raw_response.list_transactions(
                id="",
                id_type="idType",
                end_date="endDate",
                start_date="startDate",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_balance(self, async_client: AsyncAmbientSDK) -> None:
        org = await async_client.org.retrieve_balance(
            id="id",
            id_type="idType",
        )
        assert_matches_type(OrgRetrieveBalanceResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_balance(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.org.with_raw_response.retrieve_balance(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgRetrieveBalanceResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_balance(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.org.with_streaming_response.retrieve_balance(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(OrgRetrieveBalanceResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_balance(self, async_client: AsyncAmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            await async_client.org.with_raw_response.retrieve_balance(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.org.with_raw_response.retrieve_balance(
                id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_bank_info(self, async_client: AsyncAmbientSDK) -> None:
        org = await async_client.org.retrieve_bank_info(
            id="id",
            id_type="idType",
        )
        assert_matches_type(OrgRetrieveBankInfoResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_bank_info(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.org.with_raw_response.retrieve_bank_info(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgRetrieveBankInfoResponse, org, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_bank_info(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.org.with_streaming_response.retrieve_bank_info(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(OrgRetrieveBankInfoResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_bank_info(self, async_client: AsyncAmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            await async_client.org.with_raw_response.retrieve_bank_info(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.org.with_raw_response.retrieve_bank_info(
                id="",
                id_type="idType",
            )
