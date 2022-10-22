# Author Jatin Jain


# General Tree in Python
class Tree:
    def __init__(self, data=None):
        self.data = data
        self.child = []
        self.parent  = None
    
    def add_child(self, ch):
        ch.parent = self
        self.child.append(ch)
    
    def print_child(self, s = 2):
        if self.parent == None:
            print("|-" + self.data)
        for i in self.child:
            print(" "*s + "|" + "-"*(s) + i.data)
            i.print_child(s + 1)


def main():
    root = Tree("Electronics")
    laptop = Tree("Laptop")
    headphone = Tree("Headphone")
    mobile = Tree("Mobile")
    root.add_child(laptop)
    root.add_child(headphone)
    root.add_child(mobile)
    laptop.add_child(Tree("Lenovo legion 5"))
    laptop.add_child(Tree("Hp Ideal Pad"))
    laptop.add_child(Tree("Toshiba satallite"))
    headphone.add_child(Tree("Boat"))
    headphone.add_child(Tree("Jbl"))
    headphone.add_child(Tree("aliencandy"))
    mobile.add_child(Tree("Samsung A22"))
    mobile.add_child(Tree("Vivo 1724"))
    mobile.add_child(Tree("One Plus 6t"))
    root.print_child()
        

if __name__ == '__main__':
    main()





