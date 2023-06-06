from user import User
from wallet import WalletInsufficientBalanceException
from wallet import Wallet
from product import Product, PassProduct
from transaction import Transaction, TransactionItem, DeliveryTransactionItem
from address import Address
from credit import Credit


def application():
    user_1 = User(first_name=User.first_name, last_name=User.last_name, email=User.email, mobile=User.mobile)
    wallet_1 = Wallet(user=user_1, initial_balance=5.0)
    credit_1 = Credit(user=user_1, initial_balance=0)

    wallet_1.add_balance(amount=25.0)

    product_1 = Product(name='Meal A', price=7.50)
    product_2 = Product(name='Meal B', price=15.50)
    product_3 = PassProduct(name='Pass C', price=5, addition_credit=2)

    address_1 = Address(address_1='JL Jend Sudirman', postal_code='91232', city='Jakarta', country='Indonesia')
    address_2 = Address(address_1='Thompson Rd', postal_code='75021', city='Singapore', country='Singapore')

    transaction_items = []
    transaction_items.append(DeliveryTransactionItem(product=product_1, qty=5, address=address_1))
    transaction_items.append(DeliveryTransactionItem(product=product_2, qty=3, address=address_2))
    transaction_items.append(TransactionItem(product=product_3, qty=1))
    transaction_items.append(TransactionItem(product=product_3, qty=1))
    transaction = Transaction(user=user_1, payment=wallet_1, transaction_items=transaction_items)

    print('? User:', wallet_1.user.get_email())
    print('? Current credit balance:', credit_1.get_balances())
    print('? Current wallet balance:', wallet_1.get_balances())
    print('~ Topup $150')
    wallet_1.add_balance(amount=150)
    print('? Current balance:', wallet_1.get_balances())
    print('? Sub total:', transaction.calculate_total())
    print('? Delivery total:', transaction.delivery_total())
    print('? GST:', transaction.gst_total())
    print('? Grand total:', transaction.calculate_grand_total())

    print(f'~ Pass credit balance: +{transaction.get_addition_credit()}')


    try:
        transaction.proceed()
    except WalletInsufficientBalanceException as err:
        print(err)
    else:
        print('~ Paid')

    print('? Current wallet balance:', wallet_1.get_balances())



if __name__ == '__main__':
    application()
