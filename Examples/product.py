"""
 A simple implementation of opp on Product
"""

from unicodedata import name


class Product():

  def __init__(self, name, price, stock):
    # Create a private variable can only be access within the class
    self.__name = name
    self.__price = price
    self.__stock = stock

  # getter method return name
  @property
  def name(self):
    return self.__name
  
  # getter method for return price
  # We are using property decorator to help us setting up setter and getter
  # property is a python built-in function that return a function (can be use as decorator)
  @property
  def price(self):
    return self.__price
  
  # setter method for update price
  @price.setter
  def price(self, price):
    self.__price = price
  
  # getter method for return stock
  @property
  def stock(self):
    return self.__stock;

  # setter method for update stock
  @stock.setter
  def stock(self, stock):
    self.__stock = stock

  def purchaseOne(self):
    if (self.__stock > 0):
      self.__stock -= 1

  # update price according the the discount percentage
  def discount(self, percentage):
    self.__price = self.__price * (1 - percentage/100)


if __name__ == "__main__":
  
  # Create a few product
  iphone = Product('iPhone', 1200, 10)
  samsungPhone = Product('Galaxy S22', 1100, 10)

  # purchase iphone
  iphone.purchaseOne()

  # Discount price on samsung
  samsungPhone.discount(20)

  # calling setter & getter example
  iphone.price = 1234
  print(iphone.price)

  # print price of samsungPhone
  print(samsungPhone.price)

  print(iphone.stock)