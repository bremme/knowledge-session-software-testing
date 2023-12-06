from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    contract_id: int


@dataclass
class PowerDemand:
    day: str
    power: int


@dataclass
class CapacityRequest:
    customer: Customer
    capacity: list[PowerDemand]
