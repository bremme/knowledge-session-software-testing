from dataclasses import dataclass
from enum import IntEnum, auto


class ContractType(IntEnum):
    TYPE_A = auto()
    TYPE_B = auto()


@dataclass
class Contract:
    contract_type: ContractType
    firm_capacity: int
    non_firm_capacity: int
