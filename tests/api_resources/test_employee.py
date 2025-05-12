# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ambient_sdk import AmbientSDK, AsyncAmbientSDK
from tests.utils import assert_matches_type
from ambient_sdk.types import (
    EmployeeCreateResponse,
    EmployeeUpdateResponse,
    EmployeeArchiveResponse,
    EmployeeUnarchiveResponse,
    EmployeeBatchCreateResponse,
    EmployeeGetTransactionsResponse,
    EmployeeGetPaymentMethodsResponse,
)
from ambient_sdk._utils import parse_date, parse_datetime
from ambient_sdk.types.employee import Employee

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmployee:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: AmbientSDK) -> None:
        employee = client.employee.create(
            city="Phoenix",
            dob=parse_date("2019-12-27"),
            email="johndoe@gmail.com",
            employee_id="A12125",
            employer_id="E56213",
            first_name="John",
            last_name="Doe",
            org_id=5,
            phone="888-676-3244",
            ssn="123-45-6789",
            state="AZ",
            street_address1="123 Apple St",
            zip="45869",
        )
        assert_matches_type(EmployeeCreateResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: AmbientSDK) -> None:
        employee = client.employee.create(
            city="Phoenix",
            dob=parse_date("2019-12-27"),
            email="johndoe@gmail.com",
            employee_id="A12125",
            employer_id="E56213",
            first_name="John",
            last_name="Doe",
            org_id=5,
            phone="888-676-3244",
            ssn="123-45-6789",
            state="AZ",
            street_address1="123 Apple St",
            zip="45869",
            middle_name="Fred",
        )
        assert_matches_type(EmployeeCreateResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: AmbientSDK) -> None:
        response = client.employee.with_raw_response.create(
            city="Phoenix",
            dob=parse_date("2019-12-27"),
            email="johndoe@gmail.com",
            employee_id="A12125",
            employer_id="E56213",
            first_name="John",
            last_name="Doe",
            org_id=5,
            phone="888-676-3244",
            ssn="123-45-6789",
            state="AZ",
            street_address1="123 Apple St",
            zip="45869",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = response.parse()
        assert_matches_type(EmployeeCreateResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: AmbientSDK) -> None:
        with client.employee.with_streaming_response.create(
            city="Phoenix",
            dob=parse_date("2019-12-27"),
            email="johndoe@gmail.com",
            employee_id="A12125",
            employer_id="E56213",
            first_name="John",
            last_name="Doe",
            org_id=5,
            phone="888-676-3244",
            ssn="123-45-6789",
            state="AZ",
            street_address1="123 Apple St",
            zip="45869",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = response.parse()
            assert_matches_type(EmployeeCreateResponse, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: AmbientSDK) -> None:
        employee = client.employee.retrieve(
            id="id",
            id_type="idType",
        )
        assert_matches_type(Employee, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: AmbientSDK) -> None:
        response = client.employee.with_raw_response.retrieve(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = response.parse()
        assert_matches_type(Employee, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: AmbientSDK) -> None:
        with client.employee.with_streaming_response.retrieve(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = response.parse()
            assert_matches_type(Employee, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: AmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            client.employee.with_raw_response.retrieve(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employee.with_raw_response.retrieve(
                id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: AmbientSDK) -> None:
        employee = client.employee.update(
            id="id",
            id_type="idType",
        )
        assert_matches_type(EmployeeUpdateResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: AmbientSDK) -> None:
        employee = client.employee.update(
            id="id",
            id_type="idType",
            city="city",
            debit_id="debitId",
            dob=parse_date("2019-12-27"),
            email="dev@stainless.com",
            employee_id="employeeId",
            employer_id="employerId",
            first_name="Jack",
            last_name="Jones",
            org_id=0,
            owner=True,
            passport_account_id="passportAccountId",
            passport_customer_id="passportCustomerId",
            phone="phone",
            ssn="ssn",
            state="state",
            status="status",
            street_address1="streetAddress1",
            zip="zip",
        )
        assert_matches_type(EmployeeUpdateResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: AmbientSDK) -> None:
        response = client.employee.with_raw_response.update(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = response.parse()
        assert_matches_type(EmployeeUpdateResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: AmbientSDK) -> None:
        with client.employee.with_streaming_response.update(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = response.parse()
            assert_matches_type(EmployeeUpdateResponse, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: AmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            client.employee.with_raw_response.update(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employee.with_raw_response.update(
                id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_archive(self, client: AmbientSDK) -> None:
        employee = client.employee.archive(
            id="id",
            id_type="idType",
        )
        assert_matches_type(EmployeeArchiveResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_archive_with_all_params(self, client: AmbientSDK) -> None:
        employee = client.employee.archive(
            id="id",
            id_type="idType",
            admin_memo="Archived due to termination",
            archived_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            archived_reason="Terminated",
        )
        assert_matches_type(EmployeeArchiveResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_archive(self, client: AmbientSDK) -> None:
        response = client.employee.with_raw_response.archive(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = response.parse()
        assert_matches_type(EmployeeArchiveResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_archive(self, client: AmbientSDK) -> None:
        with client.employee.with_streaming_response.archive(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = response.parse()
            assert_matches_type(EmployeeArchiveResponse, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_archive(self, client: AmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            client.employee.with_raw_response.archive(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employee.with_raw_response.archive(
                id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_batch_create(self, client: AmbientSDK) -> None:
        employee = client.employee.batch_create(
            body=[
                {
                    "city": "Miami",
                    "dob": parse_date("2019-12-27"),
                    "email": "jackjones@gmail.com",
                    "employee_id": "A302",
                    "employer_id": "E21454",
                    "first_name": "Jack",
                    "last_name": "Jones",
                    "org_id": 0,
                    "phone": "928-772-5266",
                    "ssn": "111-22-3333",
                    "state": "FL",
                    "street_address1": "11 Main St",
                    "zip": "35918",
                },
                {
                    "city": "Boston",
                    "dob": parse_date("2019-12-27"),
                    "email": "twashington@gmail.com",
                    "employee_id": "A303",
                    "employer_id": "E21454",
                    "first_name": "Thomas",
                    "last_name": "Washington",
                    "org_id": 0,
                    "phone": "454-122-3780",
                    "ssn": "444-55-6666",
                    "state": "MA",
                    "street_address1": "41 Apple Ave",
                    "zip": "84712",
                },
            ],
        )
        assert_matches_type(EmployeeBatchCreateResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_batch_create(self, client: AmbientSDK) -> None:
        response = client.employee.with_raw_response.batch_create(
            body=[
                {
                    "city": "Miami",
                    "dob": parse_date("2019-12-27"),
                    "email": "jackjones@gmail.com",
                    "employee_id": "A302",
                    "employer_id": "E21454",
                    "first_name": "Jack",
                    "last_name": "Jones",
                    "org_id": 0,
                    "phone": "928-772-5266",
                    "ssn": "111-22-3333",
                    "state": "FL",
                    "street_address1": "11 Main St",
                    "zip": "35918",
                },
                {
                    "city": "Boston",
                    "dob": parse_date("2019-12-27"),
                    "email": "twashington@gmail.com",
                    "employee_id": "A303",
                    "employer_id": "E21454",
                    "first_name": "Thomas",
                    "last_name": "Washington",
                    "org_id": 0,
                    "phone": "454-122-3780",
                    "ssn": "444-55-6666",
                    "state": "MA",
                    "street_address1": "41 Apple Ave",
                    "zip": "84712",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = response.parse()
        assert_matches_type(EmployeeBatchCreateResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_batch_create(self, client: AmbientSDK) -> None:
        with client.employee.with_streaming_response.batch_create(
            body=[
                {
                    "city": "Miami",
                    "dob": parse_date("2019-12-27"),
                    "email": "jackjones@gmail.com",
                    "employee_id": "A302",
                    "employer_id": "E21454",
                    "first_name": "Jack",
                    "last_name": "Jones",
                    "org_id": 0,
                    "phone": "928-772-5266",
                    "ssn": "111-22-3333",
                    "state": "FL",
                    "street_address1": "11 Main St",
                    "zip": "35918",
                },
                {
                    "city": "Boston",
                    "dob": parse_date("2019-12-27"),
                    "email": "twashington@gmail.com",
                    "employee_id": "A303",
                    "employer_id": "E21454",
                    "first_name": "Thomas",
                    "last_name": "Washington",
                    "org_id": 0,
                    "phone": "454-122-3780",
                    "ssn": "444-55-6666",
                    "state": "MA",
                    "street_address1": "41 Apple Ave",
                    "zip": "84712",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = response.parse()
            assert_matches_type(EmployeeBatchCreateResponse, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_payment_methods(self, client: AmbientSDK) -> None:
        employee = client.employee.get_payment_methods(
            id="id",
            id_type="idType",
        )
        assert_matches_type(EmployeeGetPaymentMethodsResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_payment_methods(self, client: AmbientSDK) -> None:
        response = client.employee.with_raw_response.get_payment_methods(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = response.parse()
        assert_matches_type(EmployeeGetPaymentMethodsResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_payment_methods(self, client: AmbientSDK) -> None:
        with client.employee.with_streaming_response.get_payment_methods(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = response.parse()
            assert_matches_type(EmployeeGetPaymentMethodsResponse, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_payment_methods(self, client: AmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            client.employee.with_raw_response.get_payment_methods(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employee.with_raw_response.get_payment_methods(
                id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_transactions(self, client: AmbientSDK) -> None:
        employee = client.employee.get_transactions(
            id="id",
            id_type="idType",
            end_date="endDate",
            start_date="startDate",
        )
        assert_matches_type(EmployeeGetTransactionsResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_transactions(self, client: AmbientSDK) -> None:
        response = client.employee.with_raw_response.get_transactions(
            id="id",
            id_type="idType",
            end_date="endDate",
            start_date="startDate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = response.parse()
        assert_matches_type(EmployeeGetTransactionsResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_transactions(self, client: AmbientSDK) -> None:
        with client.employee.with_streaming_response.get_transactions(
            id="id",
            id_type="idType",
            end_date="endDate",
            start_date="startDate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = response.parse()
            assert_matches_type(EmployeeGetTransactionsResponse, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_transactions(self, client: AmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            client.employee.with_raw_response.get_transactions(
                id="id",
                id_type="",
                end_date="endDate",
                start_date="startDate",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employee.with_raw_response.get_transactions(
                id="",
                id_type="idType",
                end_date="endDate",
                start_date="startDate",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_unarchive(self, client: AmbientSDK) -> None:
        employee = client.employee.unarchive(
            id="id",
            id_type="idType",
        )
        assert_matches_type(EmployeeUnarchiveResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_unarchive(self, client: AmbientSDK) -> None:
        response = client.employee.with_raw_response.unarchive(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = response.parse()
        assert_matches_type(EmployeeUnarchiveResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_unarchive(self, client: AmbientSDK) -> None:
        with client.employee.with_streaming_response.unarchive(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = response.parse()
            assert_matches_type(EmployeeUnarchiveResponse, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_unarchive(self, client: AmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            client.employee.with_raw_response.unarchive(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employee.with_raw_response.unarchive(
                id="",
                id_type="idType",
            )


class TestAsyncEmployee:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncAmbientSDK) -> None:
        employee = await async_client.employee.create(
            city="Phoenix",
            dob=parse_date("2019-12-27"),
            email="johndoe@gmail.com",
            employee_id="A12125",
            employer_id="E56213",
            first_name="John",
            last_name="Doe",
            org_id=5,
            phone="888-676-3244",
            ssn="123-45-6789",
            state="AZ",
            street_address1="123 Apple St",
            zip="45869",
        )
        assert_matches_type(EmployeeCreateResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAmbientSDK) -> None:
        employee = await async_client.employee.create(
            city="Phoenix",
            dob=parse_date("2019-12-27"),
            email="johndoe@gmail.com",
            employee_id="A12125",
            employer_id="E56213",
            first_name="John",
            last_name="Doe",
            org_id=5,
            phone="888-676-3244",
            ssn="123-45-6789",
            state="AZ",
            street_address1="123 Apple St",
            zip="45869",
            middle_name="Fred",
        )
        assert_matches_type(EmployeeCreateResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.employee.with_raw_response.create(
            city="Phoenix",
            dob=parse_date("2019-12-27"),
            email="johndoe@gmail.com",
            employee_id="A12125",
            employer_id="E56213",
            first_name="John",
            last_name="Doe",
            org_id=5,
            phone="888-676-3244",
            ssn="123-45-6789",
            state="AZ",
            street_address1="123 Apple St",
            zip="45869",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = await response.parse()
        assert_matches_type(EmployeeCreateResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.employee.with_streaming_response.create(
            city="Phoenix",
            dob=parse_date("2019-12-27"),
            email="johndoe@gmail.com",
            employee_id="A12125",
            employer_id="E56213",
            first_name="John",
            last_name="Doe",
            org_id=5,
            phone="888-676-3244",
            ssn="123-45-6789",
            state="AZ",
            street_address1="123 Apple St",
            zip="45869",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = await response.parse()
            assert_matches_type(EmployeeCreateResponse, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        employee = await async_client.employee.retrieve(
            id="id",
            id_type="idType",
        )
        assert_matches_type(Employee, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.employee.with_raw_response.retrieve(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = await response.parse()
        assert_matches_type(Employee, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.employee.with_streaming_response.retrieve(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = await response.parse()
            assert_matches_type(Employee, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            await async_client.employee.with_raw_response.retrieve(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employee.with_raw_response.retrieve(
                id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncAmbientSDK) -> None:
        employee = await async_client.employee.update(
            id="id",
            id_type="idType",
        )
        assert_matches_type(EmployeeUpdateResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAmbientSDK) -> None:
        employee = await async_client.employee.update(
            id="id",
            id_type="idType",
            city="city",
            debit_id="debitId",
            dob=parse_date("2019-12-27"),
            email="dev@stainless.com",
            employee_id="employeeId",
            employer_id="employerId",
            first_name="Jack",
            last_name="Jones",
            org_id=0,
            owner=True,
            passport_account_id="passportAccountId",
            passport_customer_id="passportCustomerId",
            phone="phone",
            ssn="ssn",
            state="state",
            status="status",
            street_address1="streetAddress1",
            zip="zip",
        )
        assert_matches_type(EmployeeUpdateResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.employee.with_raw_response.update(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = await response.parse()
        assert_matches_type(EmployeeUpdateResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.employee.with_streaming_response.update(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = await response.parse()
            assert_matches_type(EmployeeUpdateResponse, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncAmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            await async_client.employee.with_raw_response.update(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employee.with_raw_response.update(
                id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_archive(self, async_client: AsyncAmbientSDK) -> None:
        employee = await async_client.employee.archive(
            id="id",
            id_type="idType",
        )
        assert_matches_type(EmployeeArchiveResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_archive_with_all_params(self, async_client: AsyncAmbientSDK) -> None:
        employee = await async_client.employee.archive(
            id="id",
            id_type="idType",
            admin_memo="Archived due to termination",
            archived_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            archived_reason="Terminated",
        )
        assert_matches_type(EmployeeArchiveResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.employee.with_raw_response.archive(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = await response.parse()
        assert_matches_type(EmployeeArchiveResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.employee.with_streaming_response.archive(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = await response.parse()
            assert_matches_type(EmployeeArchiveResponse, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncAmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            await async_client.employee.with_raw_response.archive(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employee.with_raw_response.archive(
                id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_batch_create(self, async_client: AsyncAmbientSDK) -> None:
        employee = await async_client.employee.batch_create(
            body=[
                {
                    "city": "Miami",
                    "dob": parse_date("2019-12-27"),
                    "email": "jackjones@gmail.com",
                    "employee_id": "A302",
                    "employer_id": "E21454",
                    "first_name": "Jack",
                    "last_name": "Jones",
                    "org_id": 0,
                    "phone": "928-772-5266",
                    "ssn": "111-22-3333",
                    "state": "FL",
                    "street_address1": "11 Main St",
                    "zip": "35918",
                },
                {
                    "city": "Boston",
                    "dob": parse_date("2019-12-27"),
                    "email": "twashington@gmail.com",
                    "employee_id": "A303",
                    "employer_id": "E21454",
                    "first_name": "Thomas",
                    "last_name": "Washington",
                    "org_id": 0,
                    "phone": "454-122-3780",
                    "ssn": "444-55-6666",
                    "state": "MA",
                    "street_address1": "41 Apple Ave",
                    "zip": "84712",
                },
            ],
        )
        assert_matches_type(EmployeeBatchCreateResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_batch_create(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.employee.with_raw_response.batch_create(
            body=[
                {
                    "city": "Miami",
                    "dob": parse_date("2019-12-27"),
                    "email": "jackjones@gmail.com",
                    "employee_id": "A302",
                    "employer_id": "E21454",
                    "first_name": "Jack",
                    "last_name": "Jones",
                    "org_id": 0,
                    "phone": "928-772-5266",
                    "ssn": "111-22-3333",
                    "state": "FL",
                    "street_address1": "11 Main St",
                    "zip": "35918",
                },
                {
                    "city": "Boston",
                    "dob": parse_date("2019-12-27"),
                    "email": "twashington@gmail.com",
                    "employee_id": "A303",
                    "employer_id": "E21454",
                    "first_name": "Thomas",
                    "last_name": "Washington",
                    "org_id": 0,
                    "phone": "454-122-3780",
                    "ssn": "444-55-6666",
                    "state": "MA",
                    "street_address1": "41 Apple Ave",
                    "zip": "84712",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = await response.parse()
        assert_matches_type(EmployeeBatchCreateResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_batch_create(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.employee.with_streaming_response.batch_create(
            body=[
                {
                    "city": "Miami",
                    "dob": parse_date("2019-12-27"),
                    "email": "jackjones@gmail.com",
                    "employee_id": "A302",
                    "employer_id": "E21454",
                    "first_name": "Jack",
                    "last_name": "Jones",
                    "org_id": 0,
                    "phone": "928-772-5266",
                    "ssn": "111-22-3333",
                    "state": "FL",
                    "street_address1": "11 Main St",
                    "zip": "35918",
                },
                {
                    "city": "Boston",
                    "dob": parse_date("2019-12-27"),
                    "email": "twashington@gmail.com",
                    "employee_id": "A303",
                    "employer_id": "E21454",
                    "first_name": "Thomas",
                    "last_name": "Washington",
                    "org_id": 0,
                    "phone": "454-122-3780",
                    "ssn": "444-55-6666",
                    "state": "MA",
                    "street_address1": "41 Apple Ave",
                    "zip": "84712",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = await response.parse()
            assert_matches_type(EmployeeBatchCreateResponse, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_payment_methods(self, async_client: AsyncAmbientSDK) -> None:
        employee = await async_client.employee.get_payment_methods(
            id="id",
            id_type="idType",
        )
        assert_matches_type(EmployeeGetPaymentMethodsResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_payment_methods(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.employee.with_raw_response.get_payment_methods(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = await response.parse()
        assert_matches_type(EmployeeGetPaymentMethodsResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_payment_methods(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.employee.with_streaming_response.get_payment_methods(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = await response.parse()
            assert_matches_type(EmployeeGetPaymentMethodsResponse, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_payment_methods(self, async_client: AsyncAmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            await async_client.employee.with_raw_response.get_payment_methods(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employee.with_raw_response.get_payment_methods(
                id="",
                id_type="idType",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_transactions(self, async_client: AsyncAmbientSDK) -> None:
        employee = await async_client.employee.get_transactions(
            id="id",
            id_type="idType",
            end_date="endDate",
            start_date="startDate",
        )
        assert_matches_type(EmployeeGetTransactionsResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_transactions(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.employee.with_raw_response.get_transactions(
            id="id",
            id_type="idType",
            end_date="endDate",
            start_date="startDate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = await response.parse()
        assert_matches_type(EmployeeGetTransactionsResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_transactions(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.employee.with_streaming_response.get_transactions(
            id="id",
            id_type="idType",
            end_date="endDate",
            start_date="startDate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = await response.parse()
            assert_matches_type(EmployeeGetTransactionsResponse, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_transactions(self, async_client: AsyncAmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            await async_client.employee.with_raw_response.get_transactions(
                id="id",
                id_type="",
                end_date="endDate",
                start_date="startDate",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employee.with_raw_response.get_transactions(
                id="",
                id_type="idType",
                end_date="endDate",
                start_date="startDate",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_unarchive(self, async_client: AsyncAmbientSDK) -> None:
        employee = await async_client.employee.unarchive(
            id="id",
            id_type="idType",
        )
        assert_matches_type(EmployeeUnarchiveResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_unarchive(self, async_client: AsyncAmbientSDK) -> None:
        response = await async_client.employee.with_raw_response.unarchive(
            id="id",
            id_type="idType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = await response.parse()
        assert_matches_type(EmployeeUnarchiveResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_unarchive(self, async_client: AsyncAmbientSDK) -> None:
        async with async_client.employee.with_streaming_response.unarchive(
            id="id",
            id_type="idType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = await response.parse()
            assert_matches_type(EmployeeUnarchiveResponse, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_unarchive(self, async_client: AsyncAmbientSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id_type` but received ''"):
            await async_client.employee.with_raw_response.unarchive(
                id="id",
                id_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employee.with_raw_response.unarchive(
                id="",
                id_type="idType",
            )
