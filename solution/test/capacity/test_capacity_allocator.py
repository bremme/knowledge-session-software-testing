from typing import Optional
from unittest.mock import MagicMock

import pytest

from app.capacity.allocator import CapacityAllocator
from app.capacity.request import CapacityRequest, Customer
from app.contract.contract import Contract, ContractType
from app.contract.repository import ContractRepositoryInterface

# Testing scope
# Only capacitor allocator

# Mocks
# Use mock for the contract inspector

# Stubs
# Use stub for the contract repository


class ContractRepositoryStub(ContractRepositoryInterface):
    def get_contract(self, contract_id: int) -> Optional[Contract]:
        return {
            1: Contract(
                contract_type=ContractType.TYPE_A,
                firm_capacity=100,
                non_firm_capacity=50,
            ),
            2: Contract(
                contract_type=ContractType.TYPE_B,
                firm_capacity=25,
                non_firm_capacity=150,
            ),
        }[contract_id]


class TestCapacityAllocator:
    @pytest.fixture
    def allocator(self):
        repository_stub = ContractRepositoryStub()
        inspector_mock = MagicMock()
        max_daily_capacity = 200
        return CapacityAllocator(
            inspector=inspector_mock,
            repository=repository_stub,
            max_daily_capacity=max_daily_capacity,
        )

    def test_allocate__power_is_allowed__allocation_is_based_on_max_daily_capacity(
        self, allocator: CapacityAllocator
    ):
        # Given
        request_one = CapacityRequest(
            customer=Customer(name="customer-1", contract_id=1),
            capacity=[("mon", 100), ("tue", 100)],
        )
        request_two = CapacityRequest(
            customer=Customer(name="customer-2", contract_id=2),
            capacity=[("mon", 150), ("tue", 75)],
        )
        allocator.inspector.power_is_allowed.return_value = True

        # When
        result_one = allocator.allocate(request_one)
        result_two = allocator.allocate(request_two)

        # Then
        assert result_one == {"mon": True, "tue": True}, "All power should be allocated"

        assert result_two == {
            "mon": False,
            "tue": True,
        }, "Only power on Tuesday should be allocated"

        assert allocator.allocations == {
            "mon": 100,
            "tue": 175,
        }, "Allocations should be equal to sum of requests when allowed"

    def test_allocate__power_not_allowed__allocation_always_false(
        self, allocator: CapacityAllocator
    ):
        # Given
        request_one = CapacityRequest(
            customer=Customer(name="customer-1", contract_id=1),
            capacity=[("mon", 100), ("tue", 100)],
        )
        request_two = CapacityRequest(
            customer=Customer(name="customer-2", contract_id=2),
            capacity=[("mon", 150), ("tue", 75)],
        )
        allocator.inspector.power_is_allowed.return_value = False

        # When
        result_one = allocator.allocate(request_one)
        result_two = allocator.allocate(request_two)

        # Then
        assert result_one == {
            "mon": False,
            "tue": False,
        }, "No power should be allocated"

        assert result_two == {
            "mon": False,
            "tue": False,
        }, "No power should be allocated"
