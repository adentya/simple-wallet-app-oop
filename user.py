class User:

    first_name = 'John'
    last_name = 'Doe'
    email = 'johndoe@example.com'
    mobile = '+628123123123'

    def __init__(self, first_name: str, last_name: str, email: str, mobile: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mobile = mobile


    def get_mobile(self):
        return self.mobile.replace('+', '')


    def get_email(self):
        return self.email


    def get_first_name(self):
        return self.first_name


    def get_last_name(self):
        return self.last_name


    @staticmethod
    def find_by_email(email: str):
        return User(first_name=User.first_name, last_name=User.last_name, email=User.email, mobile=User.mobile)

