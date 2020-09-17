class Apple:
    def __init__(self):
        self.__price = 50

    def sell(self):
        print("Selling price: {}".format(self.__price))

    def setPrice(self, price):
        self.__price = price

apple = Apple()
apple.sell()

apple.__price = 30
apple.sell()

apple.setPrice(30)
apple.sell()
