from decimal import Decimal

from user import User
from wallet import Wallet


class Credit(Wallet):

    MINIMUM_ADD_BALANCE = 1

    def __init__(self, user: User, initial_balance: Decimal = 0) -> None:
        super().__init__(user, initial_balance)


    def get_balances(self):
        return int(self.balance)

    @staticmethod
    def find_user(email: str):
        user_1 = User.find_by_email(email=User.email)
        credit_1 = Credit(user=user_1, initial_balance=0)
        return credit_1 if user_1.get_email() == email else None
