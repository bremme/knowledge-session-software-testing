from app.capacity.request import CapacityRequest
from app.contract.inspector import ContractInspector
from app.contract.repository import ContractRepository


class CapacityAllocator:
    DEFAULT_MAX_DAILY_CAPACITY = 100

    def __init__(
        self,
        repository: ContractRepository,
        inspector: ContractInspector,
        max_daily_capacity: int = DEFAULT_MAX_DAILY_CAPACITY,
    ):
        self.repository = repository
        self.inspector = inspector
        self.max_daily_capacity = max_daily_capacity
        self.allocations = {}

    def allocate(self, request: CapacityRequest) -> dict[str, bool]:
        contract = self.repository.get_contract(request.customer.contract_id)

        allocation_result = {}

        for day, power in request.capacity:
            allocation_result[day] = self._allocate_power_for_day(contract, day, power)

        return allocation_result

    def _allocate_power_for_day(self, contract, day, power):
        # check if allowed within contract
        if not self.inspector.power_is_allowed(contract, day, power):
            return False

        # check if power is available
        if not self._power_is_available(day, power):
            return False

        # update internal state
        self._allocate_power(day, power)

        return True

    def _power_is_available(self, day, power):
        if day not in self.allocations:
            return True

        if self.allocations[day] + power <= self.max_daily_capacity:
            return True

        return False

    def _allocate_power(self, day, power):
        if day not in self.allocations:
            self.allocations[day] = 0

        self.allocations[day] += power
