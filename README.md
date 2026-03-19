# 🐍 OPython-Init — Learning Object-Oriented Python

[![Learners](https://www.codetriage.com/josharsh/learning-object-oriented-python/badges/users.svg)](https://www.codetriage.com/josharsh/learning-object-oriented-python)

A beginner-friendly, example-driven course to learn **Object-Oriented Programming (OOP) in Python**. Each lesson builds on the last, using real-world analogies and working code to make concepts stick.

---

## 🎯 Who is this for?

This course is designed for anyone who:

- **Knows basic Python** (variables, loops, conditionals, functions) but hasn't learned OOP yet, **OR**
- **Knows OOP concepts** from another language (Java, C++) and wants to see how Python does things differently

> ❗ **You don't need to know OOP before starting.** That's what we're here to learn.

---

## 📋 Prerequisites

Before diving in, make sure you're comfortable with:

- Python data types: `int`, `str`, `list`, `dict`
- Writing and calling functions
- Basic control flow: `if/else`, `for` loops, `while` loops

If you're completely new to Python, consider going through [Python's official tutorial](https://docs.python.org/3/tutorial/) first, then come back here.

---

## 🗺️ Course Overview

| Lesson | Topic | What You'll Learn |
|--------|-------|-------------------|
| 1 | Introduction to Python | Python basics refresher, setting the stage |
| 2 | Using Functions | Writing reusable code with functions |
| 3 | Introduction to OOP Concepts | Classes, objects, attributes, methods |
| 4 | OOP Implementation | Inheritance, encapsulation, polymorphism |
| 5 | Web Scraping | Applying OOP to a real-world scraping project |
| 6 | String Manipulation | Common string operations and methods in Python |

---

## 📚 Lessons

### Lesson 1 — Introduction to Python

A quick refresher on Python fundamentals before we get into OOP. Covers variables, data types, and control flow to make sure everyone starts from the same place.

### Lesson 2 — Using Functions

Functions are the first step toward organized, reusable code. This lesson covers how to define functions, pass arguments, return values, and why structuring code this way matters before we move to classes.

### Lesson 3 — Introduction to OOP Concepts

Here's where OOP begins. You'll learn:

- **Class**: A blueprint for creating objects (like a cookie cutter)
- **Object**: A specific instance built from a class (like an actual cookie)
- **Attribute**: Data attached to an object (e.g., `color`, `name`)
- **Method**: A function that belongs to a class (e.g., `bark()` on a `Dog` class)

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name      # attribute
        self.breed = breed    # attribute

    def bark(self):           # method
        print(f"{self.name} says: Woof!")

my_dog = Dog("Bruno", "Labrador")
my_dog.bark()  # Output: Bruno says: Woof!
```

### Lesson 4 — OOP Implementation

Builds on Lesson 3 with the four pillars of OOP:

- **Inheritance**: A child class inheriting from a parent class
- **Encapsulation**: Keeping internal data hidden/protected
- **Polymorphism**: The same method name behaving differently across classes
- **Abstraction**: Hiding complex details and showing only what's needed

```python
class Animal:
    def speak(self):
        pass  # to be overridden

class Cat(Animal):
    def speak(self):
        return "Meow"

class Dog(Animal):
    def speak(self):
        return "Woof"

# Polymorphism in action:
for animal in [Cat(), Dog()]:
    print(animal.speak())
# Output:
# Meow
# Woof
```

### Lesson 5 — Web Scraping

A practical project that ties OOP together. You'll build a scraper using classes to organize your code — a great example of why OOP makes real projects easier to manage.

> 💡 Requires the `requests` and `BeautifulSoup` libraries. Install with:
> ```bash
> pip install requests beautifulsoup4
> ```

### Lesson 6 — String Manipulation

Python has a rich set of built-in string methods that make text processing easy. This lesson walks through the most commonly used ones.

**What is string manipulation?**
It's any operation where you read, transform, or extract parts of a string — cleaning data, formatting output, searching text, etc.

```python
text = "  Hello, World!  "

# Stripping whitespace
print(text.strip())           # "Hello, World!"

# Changing case
print(text.lower())           # "  hello, world!  "
print(text.upper())           # "  HELLO, WORLD!  "

# Checking content
print("Hello" in text)        # True
print(text.startswith("  H")) # True

# Splitting and joining
words = "apple,banana,cherry".split(",")
print(words)                  # ['apple', 'banana', 'cherry']
print(" | ".join(words))      # apple | banana | cherry

# Replacing
print(text.replace("World", "Python"))  # "  Hello, Python!  "

# Finding position of a substring
print(text.find("World"))     # 9

# Formatting strings
name = "Revati"
print(f"Hello, {name}!")      # Hello, Revati!
```

**When would you use these?**
- Cleaning scraped web data (remove extra spaces, lowercase everything)
- Parsing CSV-like text
- Building dynamic messages or file names
- Validating user input (`.isdigit()`, `.isalpha()`)

---

## 🚀 Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/josharsh/OPython-Init.git

# 2. Navigate into the folder
cd OPython-Init

# 3. Open any lesson folder and run the Python file
python "Lesson 1 - Introduction to Python/intro.py"
```

No special installation needed beyond Python 3.x, except for Lesson 5 (see note above).

---

## 🤝 Contributing

Contributions are welcome! If you find an explanation unclear, a bug in the code, or want to add an example — open an issue or submit a pull request.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting.

---

## 📄 License

This project is licensed under the [GPL-3.0 License](LICENSE).