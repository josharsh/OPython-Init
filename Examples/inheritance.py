#showing basic inheritance in Python


class mammal(object):
    #Constructor
    def __init__(self):
        self.warm_blooded = True
        self.lays_eggs = False
        self.classification = "Mammal"

    #return the attributes
    def does_lay_eggs(self):
        return self.lays_eggs

class platypus(mammal):
    #Constructor
    def __init__(self):

        mammal.__init__(self)
        self.lays_eggs = not mammal.does_lay_eggs(self)
        self.str = "Platypus"

#driver code
class driver():

    p=platypus()

    str="The {} is a {}. ".format(p.str, p.classification)

    if p.warm_blooded:
        str+="It is warm blooded "

    if p.lays_eggs:
        str+="and it lays Eggs!"

    print(str)