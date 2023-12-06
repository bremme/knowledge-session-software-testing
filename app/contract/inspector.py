from app.contract.contract import Contract, ContractType
from app.utils.utils import is_weekend


class ContractInspector:
    def power_is_allowed(self, contract: Contract, day: str, power: int) -> bool:
        maximum_power = contract.firm_capacity + contract.non_firm_capacity

        # power can never be higher than firm capacity + non-firm capacity
        if power > maximum_power:
            return False

        # power is always allowed for contract type B
        if contract.contract_type == ContractType.TYPE_B:
            return True

        if contract.contract_type == ContractType.TYPE_A:
            # firm capacity is always allowed
            if power <= contract.firm_capacity:
                return True

            # non-firm capacity is only allowed on weekends
            if is_weekend(day):
                return True

            return False
