# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ambient_sdk import AmbientSDK, AsyncAmbientSDK
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthorization:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: AmbientSDK) -> None:
        authorization = client.authorization.retrieve()
        assert_matches_type(str, authorization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: AmbientSDK) -> None:
        response = client.authorization.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authorization = response.parse()
        assert_matches_type(str, authorization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: AmbientSDK) -> None:
        with client.authorization.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authorization = response.parse()
            assert_matches_type(str, authorization, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuthorization:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        authorization = await async_client.authorization.retrieve()
        assert_matches_type(str, authorization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.authorization.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authorization = await response.parse()
        assert_matches_type(str, authorization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.authorization.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authorization = await response.parse()
            assert_matches_type(str, authorization, path=["response"])

        assert cast(Any, response.is_closed) is True
