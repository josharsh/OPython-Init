from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Processing credit card payment of ₹{amount}...")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Processing UPI payment of ₹{amount}...")

# Using the classes
payment1 = CreditCardPayment()
payment1.pay(1000)

payment2 = UPIPayment()    #Processing credit card payment of ₹1000...

payment2.pay(500)  #Processing UPI payment of ₹500...
