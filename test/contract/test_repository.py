import pytest

from app.contract.contract import ContractType
from app.contract.repository import ContractRepository, ContractRepositoryInterface


def test_contract_repository__get_contract():
    # Given
    repository = ContractRepository()

    # When
    contract_one = repository.get_contract(1)
    contract_two = repository.get_contract(2)
    non_existing_contract = repository.get_contract(99)

    # Then
    assert contract_one.contract_type == ContractType.TYPE_A
    assert contract_one.firm_capacity == 100
    assert contract_one.non_firm_capacity == 50

    assert contract_two.contract_type == ContractType.TYPE_B
    assert contract_two.firm_capacity == 25
    assert contract_two.non_firm_capacity == 150

    assert non_existing_contract is None


def test_contract_repository_interface_not_instantiable():
    # Then
    with pytest.raises(TypeError, match="Can't instantiate abstract class"):
        ContractRepositoryInterface()
