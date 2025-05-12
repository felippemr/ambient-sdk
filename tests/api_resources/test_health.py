# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ambient_sdk import AmbientSDK, AsyncAmbientSDK
from tests.utils import assert_matches_type
from ambient_sdk.types import HealthRetrieveStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHealth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_status(self, client: AmbientSDK) -> None:
        health = client.health.retrieve_status()
        assert_matches_type(HealthRetrieveStatusResponse, health, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_status(self, client: AmbientSDK) -> None:
        response = client.health.with_raw_response.retrieve_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health = response.parse()
        assert_matches_type(HealthRetrieveStatusResponse, health, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_status(self, client: AmbientSDK) -> None:
        with client.health.with_streaming_response.retrieve_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health = response.parse()
            assert_matches_type(HealthRetrieveStatusResponse, health, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHealth:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncAmbientSDK) -> None:
        health = await async_client.health.retrieve_status()
        assert_matches_type(HealthRetrieveStatusResponse, health, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.health.with_raw_response.retrieve_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        health = await response.parse()
        assert_matches_type(HealthRetrieveStatusResponse, health, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.health.with_streaming_response.retrieve_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            health = await response.parse()
            assert_matches_type(HealthRetrieveStatusResponse, health, path=["response"])

        assert cast(Any, response.is_closed) is True
