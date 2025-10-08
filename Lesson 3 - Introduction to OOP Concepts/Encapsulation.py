# -*- coding: utf-8 -*-
# Example: Encapsulation in Python

class BankAccount:
    def __init__(self, owner, balance):
        # Private attribute (cannot be accessed directly)
        self.__balance = balance
        self.owner = owner

    # Public method to view balance
    def get_balance(self):
        return self.__balance

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Deposit amount must be positive!")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.__balance}")
        else:
            print("Invalid withdrawal amount!")

# --- Using the class ---
account = BankAccount("Dathu", 5000)

# Deposit some amount
account.deposit(1000) # Deposited ₹1000. New balance: ₹6000

# Withdraw some amount
account.withdraw(2000) # Withdrew ₹2000. Remaining balance: ₹4000

# Access the balance through method (not directly)
print(f"Final Balance: ₹{account.get_balance()}") # Final Balance: ₹4000






