# Encapsulation Examples:


class Car:

    __max_speed = 0
    __name = ""

    def __init__(self):
        self.__max_speed = 300
        self.__name = "Buggati"

    def drive(self):
        print("Max speed is: " + str(self.__max_speed))


my_car = Car()
my_car.drive()
my_car.__max_speed = 10     # This will not change the value of the __max_speed to 10 since its a private variable.
my_car.drive()              # Still the output of the __max_speed will be 300.


# If you want to mutate private variable values you can create getters and setters.

class Student:

    __student_id = ""
    __name = ""

    def __init__(self):
        self.__student_id = "123"
        self.__name = "John"

    def learn(self):
        print("Student name is:" + self.__name)

    # Setter for private variable name.
    def set_name(self, name):
        self.__name = name

    # Setter for private variable id.
    def set_id(self, student_id):
        self.__student_id = student_id


student = Student()
student.learn()
student.set_name("Tom")  # Now that we are using a setter method to set the name as Tom the name will be changed as tom.
student.learn()          # Tom will be printed as student name.
