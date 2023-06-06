import decimal
from decimal import Decimal
from typing import Optional
from user import User


class WalletInsufficientBalanceException(Exception):
    pass


class WalletMinimumAddBalanceException(Exception):
    pass


class Wallet():

    MINIMUM_ADD_BALANCE = 3.0

    def __init__(self, user: User, initial_balance: Decimal = 0) -> None:
        self.user = user
        self.balance = initial_balance


    def add_balance(self, amount: Decimal):
        if amount < self.get_minimum_add_balance():
            raise WalletMinimumAddBalanceException('Below minimum.')
        self.balance += amount


    def deduct_balance(self, amount: Decimal):
        if self.balance < amount:
            raise WalletInsufficientBalanceException('Insufficient balance.')
        self.balance -= amount


    def get_balances(self):
        return round(self.balance, 2)


    def get_minimum_add_balance(self):
        return self.MINIMUM_ADD_BALANCE


    @staticmethod
    def find_user(email: str):
        user_1 = User.find_by_email(email=User.email)
        wallet_1 = Wallet(user=user_1, initial_balance=5.0)
        return wallet_1 if user_1.get_email() == email else None
