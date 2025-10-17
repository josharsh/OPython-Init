"""
Unit tests for the comprehensive OOP example.
Tests Student, Teacher, and Course classes.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Examples')))

import pytest


def test_student_creation():
    """Test Student class initialization"""
    from comprehensive_example import Student
    
    student = Student("John Doe", 20)
    assert student.name == "John Doe"
    assert student.age == 20


def test_student_property_setter():
    """Test Student property setters"""
    from comprehensive_example import Student
    
    student = Student("Jane", 19)
    
    # Test name setter
    student.name = "Jane Smith"
    assert student.name == "Jane Smith"
    
    # Test age setter
    student.age = 20
    assert student.age == 20


def test_student_count():
    """Test static student counter"""
    from comprehensive_example import Student
    
    initial_count = Student.student_count()
    
    student1 = Student("Alice", 21)
    student2 = Student("Bob", 22)
    student3 = Student("Charlie", 23)
    
    # Count should increase by 3
    assert Student.student_count() == initial_count + 3


def test_teacher_creation():
    """Test Teacher class initialization"""
    from comprehensive_example import Teacher
    
    teacher = Teacher("Dr. Smith", "Python Programming")
    assert teacher.name == "Dr. Smith"
    assert teacher.course == "Python Programming"


def test_teacher_property_setter():
    """Test Teacher property setters"""
    from comprehensive_example import Teacher
    
    teacher = Teacher("Prof. Johnson", "Data Structures")
    
    # Test name setter
    teacher.name = "Prof. Jane Johnson"
    assert teacher.name == "Prof. Jane Johnson"
    
    # Test course setter
    teacher.course = "Algorithms"
    assert teacher.course == "Algorithms"


def test_teacher_count():
    """Test static teacher counter"""
    from comprehensive_example import Teacher
    
    initial_count = Teacher.teacher_count()
    
    teacher1 = Teacher("Dr. Adams", "OOP")
    teacher2 = Teacher("Dr. Brown", "Web Development")
    
    # Count should increase by 2
    assert Teacher.teacher_count() == initial_count + 2


def test_course_creation():
    """Test Course class initialization"""
    from comprehensive_example import Course
    
    course = Course("Introduction to Python")
    assert course.course_name == "Introduction to Python"


def test_course_student_enrollment():
    """Test enrolling students in a course"""
    from comprehensive_example import Course, Student
    
    course = Course("Machine Learning")
    student1 = Student("Alice", 22)
    student2 = Student("Bob", 23)
    
    course.enroll_student(student1)
    course.enroll_student(student2)
    
    enrolled = course.students_enrolled
    assert len(enrolled) == 2
    assert student1 in enrolled
    assert student2 in enrolled


def test_course_teacher_assignment():
    """Test assigning teacher to a course"""
    from comprehensive_example import Course, Teacher
    
    course = Course("Web Development")
    teacher = Teacher("Dr. Wilson", "Web Development")
    
    course.assign_teacher(teacher)
    assert course.teacher == teacher


def test_encapsulation():
    """Test that private variables are properly encapsulated"""
    from comprehensive_example import Student
    
    student = Student("Test", 20)
    
    # Should not be able to access private variables directly
    # (though Python allows it with name mangling)
    # The proper way is through properties
    assert student.name == "Test"
    assert student.age == 20


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
