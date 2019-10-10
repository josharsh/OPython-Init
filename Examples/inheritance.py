# creating a class SchoolMember. This class takes two arguments
# name and age of the members of the school i.e., Teachers and Students
# name and age will be common to both Teachers and Students and hence
# we will inherit it to Class Teacher and Student
class SchoolMember:
    def __init__(self,name,age):
        self.name = name #stores the name
        self.age = age   #stores the age
        print("Init School Member: %s"%self.name)
        
    def introduce(self): # prints the name and age of the new Teacher or Student
        print("New %s %d"%(self.name,self.age))

# This is the class for Teacher. Teachers will have name and age
# hence we will inherit SchoolMember class as name and age are common attribute
# Teachers can also have salary which may not be common to other members of school like students
# hence we create an attribute specific to Teacher.        
class Teacher(SchoolMember): #class SchoolMember is inherited by naming it inside parenthesis.
    
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age) #invoking the method of SchoolMember class
        self.salary = salary #stores the salary
        print("Init Teacher : %s "%self.name)
        
    def introduce(self):
        SchoolMember.introduce(self)  #invoking the method of SchoolMember class
        print("Salary : %d"%(self.salary))


# This is class for Students. same as Teachers name and age is common attribute
# hence we inherit SchoolMember class. Marks is specific to Student hence
# we create addition attribute marks
class Student(SchoolMember): #class SchoolMember is inherited by naming it inside parenthesis.
    
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age) #invoking the method of SchoolMember class
        self.marks = marks  #stores the marks
        print("Init Student %s "%(self.name))
        
    def introduce(self):
        SchoolMember.introduce(self) #invoking the method of SchoolMember class
        print("Marks %d"%self.marks)

#taking input for Teacher
nameTeacher = input("Enter the name of the Teacher: ")
ageTeacher = int(input("Enter the age of the Teacher: "))
salaryTeacher = int(input("Enter the salary of the Teacher: "))

#taking input for Student
nameStudent = input("Enter the name of the Student: ")
ageStudent = int(input("Enter the age of the Student: "))
markStudent= int(input("Enter the mark of the Student: "))

# creates the object of class Teacher
t = Teacher(nameTeacher, ageTeacher, salaryTeacher)
t.introduce()

# creates the object of class Student
s = Student(nameStudent, ageStudent, markStudent)
s.introduce()