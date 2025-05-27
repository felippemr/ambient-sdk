# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ambient_sdk import AmbientSDK, AsyncAmbientSDK
from tests.utils import assert_matches_type
from ambient_sdk.types.org.employee import PaymentMethodListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentMethods:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: AmbientSDK) -> None:
        payment_method = client.org.employee.payment_methods.list(
            id="id",
            id_type="idType",
        )
        assert_matches_type(PaymentMethodListResponse, payment_method, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: AmbientSDK) -> None:
        payment_method = client.org.employee.payment_methods.list(
            id="id",
            id_type="idType",
            page=0,
        )
        assert_matches_type(PaymentMethodListResponse, payment_method, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: AmbientSDK) -> None:
        response = client.org.employee.payment_methods.with_raw_response.list(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_method = response.parse()
        assert_matches_type(PaymentMethodListResponse, payment_method, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: AmbientSDK) -> None:
        with client.org.employee.payment_methods.with_streaming_response.list(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_method = response.parse()
            assert_matches_type(PaymentMethodListResponse, payment_method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: AmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            client.org.employee.payment_methods.with_raw_response.list(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.org.employee.payment_methods.with_raw_response.list(
                id="",
                id_type="idType",
            )


class TestAsyncPaymentMethods:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncAmbientSDK) -> None:
        payment_method = await async_client.org.employee.payment_methods.list(
            id="id",
            id_type="idType",
        )
        assert_matches_type(PaymentMethodListResponse, payment_method, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAmbientSDK) -> None:
        payment_method = await async_client.org.employee.payment_methods.list(
            id="id",
            id_type="idType",
            page=0,
        )
        assert_matches_type(PaymentMethodListResponse, payment_method, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.org.employee.payment_methods.with_raw_response.list(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_method = await response.parse()
        assert_matches_type(PaymentMethodListResponse, payment_method, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.org.employee.payment_methods.with_streaming_response.list(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_method = await response.parse()
            assert_matches_type(PaymentMethodListResponse, payment_method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncAmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            await async_client.org.employee.payment_methods.with_raw_response.list(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.org.employee.payment_methods.with_raw_response.list(
                id="",
                id_type="idType",
            )
