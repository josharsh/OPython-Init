class example:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    def _protected_thing(self):
        print("protection")
    def __private_thing(self):
        print("private def")

x = example(1, 2)
x._protected_thing() # shows a warning
x.__private_thing()  # throws Attribute error saying the method does not exist
