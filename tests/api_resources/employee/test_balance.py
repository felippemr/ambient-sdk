# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ambient_sdk import AmbientSDK, AsyncAmbientSDK
from tests.utils import assert_matches_type
from ambient_sdk.types.employee import BalanceUpdateResponse, BalanceRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBalance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: AmbientSDK) -> None:
        balance = client.employee.balance.retrieve(
            id="id",
            id_type="idType",
        )
        assert_matches_type(BalanceRetrieveResponse, balance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: AmbientSDK) -> None:
        response = client.employee.balance.with_raw_response.retrieve(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(BalanceRetrieveResponse, balance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: AmbientSDK) -> None:
        with client.employee.balance.with_streaming_response.retrieve(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(BalanceRetrieveResponse, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: AmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            client.employee.balance.with_raw_response.retrieve(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employee.balance.with_raw_response.retrieve(
                id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: AmbientSDK) -> None:
        balance = client.employee.balance.update(
            id="id",
            id_type="idType",
        )
        assert_matches_type(BalanceUpdateResponse, balance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: AmbientSDK) -> None:
        balance = client.employee.balance.update(
            id="id",
            id_type="idType",
            admin_memo="Adjustment for overpayment",
            desired_amount=387.89,
        )
        assert_matches_type(BalanceUpdateResponse, balance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: AmbientSDK) -> None:
        response = client.employee.balance.with_raw_response.update(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(BalanceUpdateResponse, balance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: AmbientSDK) -> None:
        with client.employee.balance.with_streaming_response.update(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(BalanceUpdateResponse, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: AmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            client.employee.balance.with_raw_response.update(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employee.balance.with_raw_response.update(
                id="",
                id_type="idType",
            )


class TestAsyncBalance:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        balance = await async_client.employee.balance.retrieve(
            id="id",
            id_type="idType",
        )
        assert_matches_type(BalanceRetrieveResponse, balance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.employee.balance.with_raw_response.retrieve(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = await response.parse()
        assert_matches_type(BalanceRetrieveResponse, balance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.employee.balance.with_streaming_response.retrieve(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(BalanceRetrieveResponse, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            await async_client.employee.balance.with_raw_response.retrieve(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employee.balance.with_raw_response.retrieve(
                id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncAmbientSDK) -> None:
        balance = await async_client.employee.balance.update(
            id="id",
            id_type="idType",
        )
        assert_matches_type(BalanceUpdateResponse, balance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAmbientSDK) -> None:
        balance = await async_client.employee.balance.update(
            id="id",
            id_type="idType",
            admin_memo="Adjustment for overpayment",
            desired_amount=387.89,
        )
        assert_matches_type(BalanceUpdateResponse, balance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.employee.balance.with_raw_response.update(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = await response.parse()
        assert_matches_type(BalanceUpdateResponse, balance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.employee.balance.with_streaming_response.update(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(BalanceUpdateResponse, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncAmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            await async_client.employee.balance.with_raw_response.update(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employee.balance.with_raw_response.update(
                id="",
                id_type="idType",
            )
