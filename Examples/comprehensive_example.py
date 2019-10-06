"""
This is a comprehensive example of classes, instantiating its objects
inside another class, and using its properties, static variables and static methods
"""


class Student(object):
    # this is a static or class variable
    __student_count = 0

    # this is the constructor. Note that self implies that specific
    # instance or object of the class
    def __init__(self, name, age):
        # here, we assign the name and age given through the constructor
        # to the instance variables name and age respectively
        self.__name = name
        self.__age = age
        Student.__student_count += 1

    # use properties to get and set a private variable - data encapsulation
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @staticmethod
    def student_count():
        return Student.__student_count


# Now, let's create a teacher class
class Teacher(object):
    # this is again a static or class variable
    __teacher_count = 0

    # constructor
    def __init__(self, name, course):
        # let's use __ to represent private variables
        self.__name = name
        self.__course = course
        Teacher.__teacher_count += 1

    # use properties to get and set a private variable - data encapsulation
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, course):
        self.__course = course

    @staticmethod
    def teacher_count():
        return Teacher.__teacher_count


# Next, let's create a course class
class Course(object):
    # class variable
    __course_count = 0

    # constructor
    def __init__(self, course_name):
        self.__course_name = course_name
        # let's store an array of students enrolled for a specific course
        self.__students_enrolled = []
        self.__teacher = None
        Course.__course_count += 1

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, name):
        self.__course_name = name

    @property
    def students_enrolled(self):
        return self.__students_enrolled

    @students_enrolled.setter
    def students_enrolled(self, students):
        self.__students_enrolled = students

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        self.__teacher = teacher

    # static, since it needs to be called independent of the object
    @staticmethod
    def course_count():
        return Course.__course_count


# Let's create a class for Degree
class Degree(object):
    # a static/class variable
    __degree_count = 0

    # constructor
    def __init__(self, name):
        self.__degree_name = name
        self.__courses = []
        Degree.__degree_count += 1

    @property
    def degree_name(self):
        return self.__degree_name

    @degree_name.setter
    def degree_name(self, name):
        self.__degree_name = name

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, courses):
        self.__courses = courses

    @staticmethod
    def degree_count():
        return Degree.__degree_count


# Let's create a class for University Program
class Program(object):
    # static variable
    __program_count = 0

    # constructor
    def __init__(self, name):
        self.__program_name = name
        self.__degrees = []
        Program.__program_count += 1

    @property
    def program(self):
        return self.__program_name

    @program.setter
    def program(self, name):
        self.__program_name = name

    @property
    def degrees(self):
        return self.__degrees

    @degrees.setter
    def degrees(self, degrees):
        self.__degrees = degrees

    @staticmethod
    def program_count():
        return Program.__program_count


# main entry point function
def main():
    # Let's create four students
    joe = Student("Joe", 15)
    mark = Student("Mark", 16)
    anjali = Student("Anjalee", 14)
    sweta = Student("Sweta", 15)

    # Let's create four teachers
    abhilash = Teacher("Abhilash", "Digital Signal Processing")
    paul = Teacher("Paul", "Signals and Systems")
    raghu = Teacher("Raghu", "Electronic Circuits")
    george = Teacher("George", "Logic Design")

    # Let's create 2 courses and assign students for each course and a teacher
    digital_signal_processing = Course("Digital Signal Processing")
    # can also use .append() method of list
    digital_signal_processing.students_enrolled = [joe, mark, sweta]
    digital_signal_processing.teacher = abhilash

    signals_systems = Course("Signals and Systems")
    # one can also use .append() method of list for this
    signals_systems.students_enrolled = [george, mark, anjali]

    signals_systems.teacher = paul

    # Let's now create a degree
    btech = Degree("Bachelor of Technology")
    # add students to the degree
    btech.courses.append(digital_signal_processing)
    btech.courses.append(signals_systems)
    # Finally, create a program
    ece = Program("Electronics and Communication Engineering")
    ece.degrees.append(btech)

    # Let's display some info!
    print('No. of students: {0}'.format(Student.student_count()))
    print('No. of teachers: {0}'.format(Teacher.teacher_count()))
    print('No. of courses: {0}'.format(Course.course_count()))
    # Students enrolled in course Digital Signal Processing Course:
    for course in btech.courses:
        students = [student.name for student in course.students_enrolled]
        print('Students enrolled in {0} course: {1}'.format(course.course_name, students))


# use this if you want to run the code following this only from
# within your current script!
if __name__ == '__main__':
    main()
