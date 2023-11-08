class Person:
    #Method constuct
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Method that returns if a person is of legal age
    def is_older_of_age(self):
        return True if self.age >= 22 else False

    #Method that returns older age
    def is_older(self, ObjPerson):
        return  self.age if self.age > ObjPerson.age else ObjPerson.age
            
    
#Instance objects
person1 = Person('Anny Harrys', 27)
person2 = Person('Henry Cavil', 18)

print(person2.is_older(person1))
