# Raising Exceptions in Python
# In Python programming, exceptions are raised when errors occur at runtime. We
# can also manually raise exceptions using the raise keyword. We can optionally
# pass values to the exception to clarify why that exception was raised. Given below
# are some examples to help you understand this better

# >>> raise KeyboardInterrupt
# Traceback (most recent call last):
# ...
# KeyboardInterrupt
# >>> raise MemoryError("This is an argument")
# Traceback (most recent call last):
# ...
# MemoryError: This is an argument

try:
    a = -2
 if a <= 0:
 raise ValueError("That is not a positive number!")
except ValueError as ve:
 print(ve)
