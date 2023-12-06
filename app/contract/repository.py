from abc import ABC, abstractmethod
from typing import Optional

from app.contract.contract import Contract, ContractType

CONTRACTS = {
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
}


class ContractRepositoryInterface(ABC):
    @abstractmethod
    def get_contract(self, contract_id: int) -> Optional[Contract]:  # pragma: no cover
        raise NotImplementedError


class ContractRepository(ContractRepositoryInterface):
    def get_contract(self, contract_id: int) -> Optional[Contract]:
        return CONTRACTS.get(contract_id, None)
