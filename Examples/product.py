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
  def getName(self):
    return self.__name
  
  # getter method for return price
  def getPrice(self):
    return self.__price
  
  # setter method for update price
  def setPrice(self, price):
    self.price = price
  
  # getter method for return stock
  def getStock(self):
    return self.__stock;

  # setter method for update stock
  def setStock(self, stock):
    self.__stock = stock

  def purchaseOne(self):
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

  # print price of samsungPhone
  print(samsungPhone.getPrice())

  print(iphone.getStock())