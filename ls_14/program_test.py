import pytest

from program import BankAccount , InsufficientFundsError 

@pytest.fixture
def bank_account():
    
    return BankAccount(100) 

def test_initial_balance(bank_account):
    # Проверка начального баланса
    assert bank_account.get_balance() == 100

def test_add_balance(bank_account):
    # Проверка начального баланса
    bank_account.deposit(30)
    assert bank_account.get_balance() == 130


def test_remove_balance(bank_account):
    # Проверка начального баланса
    bank_account.withdraw(30)
    assert bank_account.get_balance() == 70

def test_withdraw_insufficient_funds(bank_account):
# Проверка снятия больше средств, чем доступно
    with pytest.raises(InsufficientFundsError):
        bank_account.withdraw(200)

def test_deposit_negative_amount(bank_account):

    with pytest.raises(ValueError):
        bank_account.deposit(-30)