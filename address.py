class Address:

    def __init__(self, address_1: str, postal_code: str, city: str, country: str, address_2: str = None) -> None:
        self.address_1 = address_1
        self.address_2 = address_2
        self.postal_code = postal_code
        self.city = city
        self.country = country


    def get_address(self):
        return self.address_1 + (' ' + self.address_2.strip() if self.address_2 else '')


    def get_postal_code(self):
        return self.postal_code


    def get_city(self):
        return self.city


    def get_country(self):
        return self.country

