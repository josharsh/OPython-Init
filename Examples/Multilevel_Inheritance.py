"""
This is an example of Multilevel Inheritance

Instructions:
- Create a class Person with Name, Age & Sex
- Create a class Employee which inherits from Person and has properties Id, Salary & Department
- Create a class Manager which inherits from Employee and has properties List of Reportees
- The Employee class inherits from Person, so it gets all the properties of Person class
- The Manager class inherits from Employee so it gets all properties of Employees as well as Person class
"""


class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def print_details(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Sex: {}".format(self.sex))


class Employee(Person):
    """
    Employee class inherits from Person
    """
    employee_count = 0

    def __init__(self, name, age, sex, department):
        super().__init__(name, age, sex)
        self.department = department
        Employee.employee_count = Employee.employee_count + 1
        self.id = Employee.employee_count
        self.manager = None
        print("Employee Added : Id {} Name {}".format(self.id, self.name))

    def print_details(self):
        print("Id: {}".format(self.id))
        super().print_details()
        print("Department: {}".format(self.department))

    def print_manager(self):
        print("{} reports to {}".format(self.name, self.manager.name))


class Manager(Employee):
    """
    Manager class inherits from Employee because every Manager is also an Employee
    """
    def __init__(self, name, age, sex, department):
        super().__init__(name, age, sex, department)
        self.reportees = []

    def print_details(self):
        print("\nTeam Information")
        super().print_details()
        self.print_reportees()

    def add_reportee(self, reportee):
        reportee.manager = self
        self.reportees.append(reportee)
        print("{} now reports to {}".format(reportee.name, self.name))

    def print_reportees(self):
        print("Employees reporting to {} are:".format(self.name))
        for employee in self.reportees:
            employee.print_details()


def main():
    # Lets create few employees
    joe = Employee("Joe", 25, "M", "Tech")
    mark = Employee("Mark", 26, "M", "Finance")
    anjali = Employee("Anjalee", 24, "F", "Tech")
    sweta = Employee("Sweta", 29, "F", "Tech")

    # Lets create few Managers
    abhilash = Manager("Abhilash",32, "M", "Finance")
    paul = Manager("Paul", 28, "M", "Tech")

    # Mark reports to Abhilash
    abhilash.add_reportee(mark)

    # Lets add reportees to paul
    paul.add_reportee(joe)
    paul.add_reportee(anjali)
    paul.add_reportee(sweta)

    # Let's display some info!
    abhilash.print_details()
    paul.print_details()


# To run the code
if __name__ == '__main__':
    main()
