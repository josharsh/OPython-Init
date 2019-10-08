class SchoolMember:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Init School Member: %s"%self.name)
        
    def introduce(self):
        print("New %s %d"%(self.name,self.age))
        
class Teacher(SchoolMember):
    
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print("Init Teacher : %s "%self.name)
        
    def introduce(self):
        SchoolMember.introduce(self)
        print("Salary : %d"%(self.salary))

class Student(SchoolMember):
    
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print("Init Student %s "%(self.name))
        
    def introduce(self):
        SchoolMember.introduce(self)
        print("Marks %d"%self.marks)

nameTeacher = input("Enter the name of the Teacher: ")
ageTeacher = int(input("Enter the age of the Teacher: "))
salaryTeacher = int(input("Enter the salary of the Teacher: "))
nameStudent = input("Enter the name of the Student: ")
ageStudent = int(input("Enter the age of the Student: "))
markStudent= int(input("Enter the mark of the Student: "))
t = Teacher(nameTeacher, ageTeacher, salaryTeacher)
t.introduce()

s = Student(nameStudent, ageStudent, markStudent)
s.introduce()