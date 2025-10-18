print("Python is awesome".capitalize())
print("PYTHON IS KING".lower())
print("python is hot".upper())
print("Harry potter and the half-blood prince".title())
print("AVENGER:the war of infinity".swapcase())


text = "python is FUN"
result = text.capitalize()
print("Original:", text)
print("After capitalize():", result)

text2 = "123hello world"
print("\nOriginal:", text2)
print("After capitalize():", text2.capitalize())

text3 = "   hello world"
print("\nOriginal with spaces:", repr(text3))
print("After capitalize():", repr(text3.capitalize()))

"""
This lesson explains the .capitalize() string method in Python.

Key Points:
1. Converts the first character to uppercase if it is a letter.
2. Converts all other characters to lowercase.
3. If the first character is not a letter (e.g., space, number, symbol),
   no capitalization occurs.
"""