# Abstraction Example:

from abc import ABC, abstractmethod


# Payment is an abstract class.
class Payment(ABC):
    def print_slip(self, amount):
        print('Purchase of amount - ', amount)

    @abstractmethod
    def payment(self, amount):
        pass


# CreditCardPayment is a subclass that extends the abstract superclass Payment.
class CreditCardPayment(Payment):
    def payment(self, amount):
        print('Credit card payment of - ', amount)


# MobileWalletPayment is a subclass that extends the abstract superclass Payment.
class MobileWalletPayment(Payment):
    def payment(self, amount):
        print('Mobile wallet payment of - ', amount)


# obj = Payment()  This will cause errors since abstract classes cannot be instantiated.

obj = CreditCardPayment()
obj.payment(100)
obj.print_slip(100)

obj = MobileWalletPayment()
obj.payment(200)
obj.print_slip(200)
