# Learning-Object-Oriented-Python
![](https://www.codetriage.com/josharsh/learning-object-oriented-python/badges/users.svg)
This repository walks you through the Object Oriented Programming in python. Illustrates real world examples, working codes and going about finding a coding solution. 

# OPython-Init

A beginner-friendly collection of **Object-Oriented Programming (OOP)** examples in Python.

This repository aims to help learners **understand OOP concepts in Python through simple, clear, and practical code examples**.  
It’s designed for students, self-learners, and anyone transitioning from procedural programming to Python OOP.

---

## 👥 Who Is This For?

This repository is best suited for:

- 🧑‍💻 Beginners who already know **basic Python syntax** (variables, loops, conditionals, functions)
- 💡 Learners who understand **OOP concepts theoretically** but want to see how they work in Python
- 📚 Students preparing for programming assignments or building their first Python projects

If you’ve just started learning Python and want to move beyond basic scripting — this repo is for you!

---

## 📘 Prerequisites

Before exploring the lessons, make sure you are familiar with:

- Writing and running Python scripts (`.py` files)
- Basic concepts like:
  - Variables and Data Types
  - Lists, Tuples, Dictionaries, and Sets
  - Functions and Parameters
  - If-Else Statements and Loops

If you’re missing these, you can review the new lesson:
[`Lesson_DataStructures.py`](./Lesson_DataStructures.py)

---

## 🎯 Learning Goals

By the end of these lessons, you will:

- Understand how **classes** and **objects** work in Python  
- Learn how to use **constructors (`__init__`)** and **instance variables**  
- Implement **inheritance, polymorphism, and encapsulation**  
- Know how to organize and reuse code using OOP design  
- Write **real-world examples** that use OOP principles effectively

---

## 🧩 Repository Structure

| Folder / File | Description |
|----------------|-------------|
| `Lesson_1_Introduction.py` | Basics of Python syntax |
| `Lesson_2_ClassesObjects.py` | Classes and Objects explained |
| `Lesson_3_Inheritance.py` | Inheritance and subclassing |
| `Lesson_4_Polymorphism.py` | How methods behave differently in subclasses |
| `Lesson_5_Encapsulation.py` | Private and protected members |
| `Lesson_6_Abstraction.py` | Abstract classes and interfaces |
| `Lesson_DataStructures.py` | *(New)* Basic Data Structures in Python |
| `Lesson_StringMethods.py` | *(New)* Common String Methods like `.capitalize()` |

---

## 🧠 Example Lesson Format

Each lesson follows this format for clarity:

1. **Concept Introduction** — short description of what’s being taught  
2. **Code Example** — simple, syntax-highlighted Python code  
3. **Explanation** — plain-English breakdown of what happens  
4. **Try It Yourself** — small challenge or modification to practice


# Example: Defining a Class
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I'm {self.name}")

student1 = Student("Aarav")

student1.greet()