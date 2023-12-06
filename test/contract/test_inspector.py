import pytest

from app.contract.contract import Contract, ContractType
from app.contract.inspector import ContractInspector


# Every test should use a new instance of the inspector
@pytest.fixture
def inspector():
    return ContractInspector()


# Testing scope
# the `is_weekend`` function will be part of the unit under test. Using a mock will only complicate the test

# Mocks

# Stubs


@pytest.mark.parametrize(
    "contract_type,expected_result",
    [(ContractType.TYPE_A, False), (ContractType.TYPE_B, False)],
)
def test_power_is_allowed__power_exceeded_maximum_power__not_allowed(
    inspector: ContractInspector, contract_type: ContractType, expected_result: bool
):
    # given
    contract = Contract(
        contract_type=contract_type, firm_capacity=100, non_firm_capacity=100
    )

    # when
    allowed = inspector.power_is_allowed(contract, day="mon", power=500)

    # then
    assert allowed is expected_result


@pytest.mark.parametrize(
    "day",
    [
        ("mon"),
        ("tue"),
        ("wed"),
        ("thu"),
        ("fri"),
        ("sat"),
        ("sun"),
    ],
)
def test_power_is_allowed__contract_type_b___always_allowed(inspector, day):
    # given
    contract = Contract(
        contract_type=ContractType.TYPE_B, firm_capacity=100, non_firm_capacity=100
    )

    # when
    allowed = inspector.power_is_allowed(contract, day=day, power=200)

    # then
    assert allowed is True


@pytest.mark.parametrize(
    "day",
    [
        ("mon"),
        ("tue"),
        ("wed"),
        ("thu"),
        ("fri"),
        ("sat"),
        ("sun"),
    ],
)
def test_power_is_allowed__type_a_firm_capacity_any_day__allowed(inspector, day):
    # given
    contract = Contract(
        contract_type=ContractType.TYPE_A, firm_capacity=100, non_firm_capacity=100
    )

    # when
    allowed = inspector.power_is_allowed(contract, day=day, power=90)

    # then
    assert allowed is True


@pytest.mark.parametrize(
    "day,expected_result",
    [
        ("mon", False),
        ("tue", False),
        ("wed", False),
        ("thu", False),
        ("fri", False),
        ("sat", True),
        ("sun", True),
    ],
)
def test_power_is_allowed__type_a_non_firm_capacity_weekend__allowed(
    inspector, day, expected_result
):
    # given
    contract = Contract(
        contract_type=ContractType.TYPE_A, firm_capacity=100, non_firm_capacity=100
    )

    # when
    allowed = inspector.power_is_allowed(contract, day=day, power=120)

    # then
    assert allowed is expected_result
