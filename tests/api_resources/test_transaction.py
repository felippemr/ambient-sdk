# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ambient_sdk import AmbientSDK, AsyncAmbientSDK
from tests.utils import assert_matches_type
from ambient_sdk.types import (
    QueueTransaction,
    TransactionRetrieveResponse,
    TransactionBatchQueueResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransaction:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: AmbientSDK) -> None:
        transaction = client.transaction.retrieve(
            "id",
        )
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: AmbientSDK) -> None:
        response = client.transaction.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: AmbientSDK) -> None:
        with client.transaction.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: AmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.transaction.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_batch_queue(self, client: AmbientSDK) -> None:
        transaction = client.transaction.batch_queue(
            body=[{}, {}],
        )
        assert_matches_type(TransactionBatchQueueResponse, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_batch_queue(self, client: AmbientSDK) -> None:
        response = client.transaction.with_raw_response.batch_queue(
            body=[{}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionBatchQueueResponse, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_batch_queue(self, client: AmbientSDK) -> None:
        with client.transaction.with_streaming_response.batch_queue(
            body=[{}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionBatchQueueResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_queue(self, client: AmbientSDK) -> None:
        transaction = client.transaction.queue()
        assert_matches_type(QueueTransaction, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_queue_with_all_params(self, client: AmbientSDK) -> None:
        transaction = client.transaction.queue(
            admin_memo="Scheduled bonus payment",
            amount=207.12,
            from_account="4928588",
            to_account="4928589",
        )
        assert_matches_type(QueueTransaction, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_queue(self, client: AmbientSDK) -> None:
        response = client.transaction.with_raw_response.queue()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(QueueTransaction, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_queue(self, client: AmbientSDK) -> None:
        with client.transaction.with_streaming_response.queue() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(QueueTransaction, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTransaction:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        transaction = await async_client.transaction.retrieve(
            "id",
        )
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.transaction.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.transaction.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.transaction.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_batch_queue(self, async_client: AsyncAmbientSDK) -> None:
        transaction = await async_client.transaction.batch_queue(
            body=[{}, {}],
        )
        assert_matches_type(TransactionBatchQueueResponse, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_batch_queue(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.transaction.with_raw_response.batch_queue(
            body=[{}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionBatchQueueResponse, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_batch_queue(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.transaction.with_streaming_response.batch_queue(
            body=[{}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionBatchQueueResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_queue(self, async_client: AsyncAmbientSDK) -> None:
        transaction = await async_client.transaction.queue()
        assert_matches_type(QueueTransaction, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_queue_with_all_params(self, async_client: AsyncAmbientSDK) -> None:
        transaction = await async_client.transaction.queue(
            admin_memo="Scheduled bonus payment",
            amount=207.12,
            from_account="4928588",
            to_account="4928589",
        )
        assert_matches_type(QueueTransaction, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_queue(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.transaction.with_raw_response.queue()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(QueueTransaction, transaction, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_queue(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.transaction.with_streaming_response.queue() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(QueueTransaction, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True
