from abc import ABC, abstractmethod
from decimal import Decimal


class AbstractProduct(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass


    @abstractmethod
    def get_price(self) -> Decimal:
        return 0


    @abstractmethod
    def get_addition_credit(self) -> int:
        return 0



class Product(AbstractProduct):

    def __init__(self, name: str, price: Decimal = 0) -> None:
        self.name = name
        self.price = price


    def get_name(self):
        return self.name


    def get_price(self):
        return self.price


    def get_addition_credit(self) -> Decimal:
        return super().get_addition_credit()



class PassProduct(Product):

    def __init__(self, name: str, addition_credit: int, price: Decimal = 0) -> None:
        super().__init__(name, price)
        self.addition_credit = addition_credit


    def get_addition_credit(self):
        return self.addition_credit


