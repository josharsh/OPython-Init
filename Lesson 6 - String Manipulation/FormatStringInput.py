import string  # make sure that you import string to utilize the .capwords() method

favColor = input("What is your favorite color?:-").upper()  # makes every letter CAPITAL
print(favColor)

# or

favColor = input("What's your favorite color?:-")
print(favColor.capitalize())  # will capitalize first character and convert all other characters to lower case. Does
# not work if the first character is not a letter (empty space, number, etc.). See example below:

capitalizeExample = "the quick brown FOX jumps ovEr the lazy DOG"  # this will print when you run the file, but take note of the formatting
print('This is the string prior to calling the .capitalize() method on it: -->',
      capitalizeExample)  # this is the string
# prior to calling the capitalize method on it
print('This is what happens after calling .capitalize() on the string: -->', capitalizeExample.capitalize())

# or

favColor = input("What's are your favorite colors?:-")
print(string.capwords(
    favColor))  # utilize string.capwords() method from Python library to make the first letter of every word capitalized
