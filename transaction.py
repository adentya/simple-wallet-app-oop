from abc import ABC, abstractmethod

from decimal import Decimal
from typing import List
from product import Product
from wallet import Wallet
from address import Address
from user import User
from credit import Credit


class AbstractTransactionItem(ABC):

    @abstractmethod
    def calculate_delivery_fee(self) -> Decimal:
        return 0



class TransactionItem(AbstractTransactionItem):

    def __init__(self, product: Product, qty: int = 1) -> None:
        self.product = product
        self.qty = qty


    def __str__(self) -> str:
        return self.product.get_name()


    def calculate_delivery_fee(self) -> Decimal:
        return super().calculate_delivery_fee()


class DeliveryTransactionItem(TransactionItem):

    DELIVERY_FEE = 4

    def __init__(self, product: Product, address: Address, qty: int = 1) -> None:
        super().__init__(product, qty)
        self.address = address


    def calculate_delivery_fee(self):
        surcharge = 8
        if self.address.get_postal_code()[:2] in ['90', '91', '92']:
            surcharge = 3
        elif self.address.get_postal_code()[:2] in ['70', '71', '72']:
            surcharge = 2.50
        elif self.address.get_postal_code()[:2] in ['73', '74', '75']:
            surcharge = 1.50

        if self.qty == 1:
            return self.DELIVERY_FEE + surcharge
        elif self.qty < 4:
            return self.DELIVERY_FEE - 1 + surcharge
        elif self.qty < 6:
            return self.DELIVERY_FEE - 2 + surcharge
        elif self.qty > 6:
            return self.DELIVERY_FEE - 4 + surcharge
        else:
            return 0


class Transaction:

    def __init__(self, user: User, payment: Wallet, transaction_items: List[AbstractTransactionItem]) -> None:
        self.payment = payment
        self.transaction_items = transaction_items
        self.user = user

    def calculate_total(self) -> Decimal:
        return sum([(transaction_item.product.get_price() * transaction_item.qty) for transaction_item in self.transaction_items])

    def calculate_grand_total(self) -> Decimal:
        return self.calculate_total() + self.delivery_total() + self.gst_total()


    def delivery_total(self) -> Decimal:
        return sum([transaction_item.calculate_delivery_fee() for transaction_item in self.transaction_items])


    def gst_total(self) -> Decimal:
        return (self.calculate_total() + self.delivery_total()) * (8 / 100)


    def get_addition_credit(self):
        return sum([transaction_item.product.get_addition_credit() for transaction_item in self.transaction_items])


    def proceed(self):
        self.payment.deduct_balance(amount=self.calculate_grand_total())

        # User yang membeli pass, tambahkan juga credit balancenya.
        credit_obj = Credit.find_user(email=self.user.get_email())
        credit_obj.add_balance(amount=self.get_addition_credit())

