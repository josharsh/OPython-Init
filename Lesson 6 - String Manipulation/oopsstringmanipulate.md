# String Manipulation in Python

(Source:- [https://www.javatpoint.com/string-manipulation-in-python](https://www.javatpoint.com/string-manipulation-in-python))

In this tutorial, we will learn some cool operations to manipulate the string. We will see how we can manipulate the string in a 
Pythonic way. Strings are fundamental and essential data structures that every Python programmer works with. In Python, a string 
is a sequence of characters enclosed within either single quotes ('...') or double quotes ("..."). It is an immutable built-in data 
structure, meaning once a string is created, it cannot be modified. However, we can create new strings by concatenating or slicing 
existing strings.

Now let's understand the well-known Python string operation tricks.


## 1. String Padding: Add Extra Character Elegantly

String padding is a term for adding characters to the beginning or end of a string until it reaches a certain length. It can be useful
in formatting text to align with other data or to make it easier to read.

In Python, you can pad a string using the str.ljust(), str.rjust(), and str.center() methods.

Here's an example of padding a string with spaces using the str.ljust() method:

### Example -
```

text = "Python"  
padded_text = text.ljust(10)  
print(padded_text)

```
### Output -
```

Python

```
In the above example, the ljust() method adds spaces to the end of the string until it is ten characters long.

We can also specify the padding character by passing it as an argument to the method:

### Output -
```

----Python

```
In this example, the rjust() method adds dashes to the beginning of the string until it is ten characters long.

The str.center() method can be used to center the string within a certain width:

### Example -
```

text = "Python"  
padded_text = text.center(10, '*')  
print(padded_text)

``` 
### Output:
```

**Python**

```


## 2. String Splitting

String splitting refers to dividing a string into multiple substrings based on a specified delimiter or separator. In Python, 
you can split a string using the str.split() method.

Here's an example of splitting a string based on whitespace characters.

### Example -
```

text = "Hello world, how are you today?"  
words = text.split()  
print(words)

```
Output:
```

['Hello', 'world,', 'how', 'are', 'you', 'today?']

```
In this example, the split() method returns a list of substrings, where each substring corresponds to a word in the original string.

We can also specify a different separator to split the string:

### Example -
```

text = "apple,banana,orange,grape"  
fruits = text.split(',')  
print(fruits)

```
Output:
```

['apple', 'banana', 'orange', 'grape']

```
In the above example, the split() method splits the string based on commas and returns a list of substrings, where each substring
corresponds to a fruit in the original string.

By default, the split() method splits the string based on whitespace characters. However, you can also specify a different 
separator using the sep argument.

### Example -
```

text = "apple-banana-orange-grape"  
fruits = text.split('-', maxsplit=2)  
print(fruits)

```
In this example, the split() method splits the string based on dashes (-) and returns a list of substrings, where the first two
substrings correspond to the first and second fruits, and the third substring corresponds to the remaining fruits. The maxsplit
argument specifies the maximum number of splits to perform.


## 3. Use F-Strings for String Formatting

The f-strings are a feature in Python 3.6 and above that allows the embedding of expressions inside string literals. They are a
convenient way to create strings containing dynamic values or format strings with variable values. Let's understand the following example.

### Example -
```

name = "Alice"  
age = 30  
greeting = f"Hello, my name is {name} and I'm {age} years old."  
print(greeting)

```
### Output -
```

Hello, my name is Alice and I'm 30 years old.

```
We can also format value in a specific way.
### Example -
```

price = 12.3456  
formatted_price = f"The price is ${price:.2f}"  
print(formatted_price)

```
### Output -
```

The price is $12.35

```


## 4. Eliminating Unnecessary Character of a String
Python's strip() method is useful for data cleaning, especially when removing unnecessary characters from the beginning or
end of strings. Data scientists often find data cleaning tedious, but Python's built-in string manipulation methods make it
easier to remove unwanted characters from strings. The strip() method, in particular, can remove leading or trailing 
characters from a string.

### Example -
```

text = "!!!Hello, World!!!"  
clean_text = text.strip("!")  
print(clean_text)

``` 
### Output -
```

Hello, World

```
Explanation -

In the above code, the strip() method is used to remove the exclamation marks (!) from the beginning and end of the text string.
The resulting string, clean_text, contains only the text content without any unnecessary characters.

Note that the strip() method only removes characters from the beginning and end of a string. If you want to remove characters from
within a string, you can use other string manipulation methods, such as replace() or regular expressions.


## 5. Concatenate Strings
In Python, we can concatenate strings using the + operator. Below is an example:

### Example -
```

string1 = "Hello"  
string2 = "world"  
result = string1 + " " + string2  
print(result)

``` 
### Output -
```

Hello world

```
In the above example, we first define two strings string1 and string2. We then concatenate them using the + operator 
and add a space between them to create a new string called result. Finally, we print out the result string using the 
print() function.

In another way, we can use the join() method to concatenate strings. Let's understand the following example.

### Example -
```

delimiter = " "  
my_list = ["apple", "banana", "cherry"]  
result = delimiter.join(my_list)  
print(result)

``` 
### Output -
```

apple banana cherry

```
In the above code, we first define a delimiter variable, which is set to a space character. We then define a list called my_list,
which contains three strings. We use the join() method on the delimiter variable, passing in the my_list list as an argument.
The join() method joins the strings in the my_list list together with the delimiter between them and returns a new string called result.
Finally, we print out the result string using the print() function.


## 6. Search for Substring Effective
Finding search string is a common requirement in daily programming. Python comes with the two methods. One is find() method -

### Example -
```

title = 'How to search substrings of Python strings'  
print(title.find('string'))  
print(title.find('string'))  
print(title.find('Yang'))

```
### Output - 
```

17
35

```
The second method is index() -

### Example -
```

title = 'How to search substrings of Python strings'  
print(title.index('string'))  
print(title.index('string'))  
print(title.index('Yang'))

```
### Output - 
```

17
35
# ValueError: substring not found

```
As we can see, Python's find() method returned -1 in case of string not found. However, index() method raised an error.


## 7. Leverage Regular Expression for Complex String Handling
Regular expressions (regex) are a powerful tool for handling complex string manipulation tasks in Python. They allow us to 
search for patterns within strings, extract information, and perform substitutions based on those patterns.

To use regex in Python, we first need to import the re module. Here's a simple example of using regex to search for a
pattern in a string:

Let's understand the following example.

### Example -
```

import re  
string = "The quick brown fox jumps over the lazy dog."  
pattern = r"fox"  
match = re.search(pattern, string)  
if match:  
    print("Match found!")  
else:  
    print("Match not found.")

```
### Output -
```

Match Found

```
Explanation -

In the above code, we search for the pattern "fox" in the string "The quick brown fox jumps over the lazy dog." The re.search()
function returns a match object if the pattern is found, and None otherwise. We use an if statement to check if a match was
found, and print the appropriate message.

Let's understand another example of using regex in Python -

### Example -
```

import re  
string = "John Doe (42 years old)"  
pattern = r"(\w+) (\w+) \((\d+) years old\)"  
match = re.search(pattern, string)  
if match:  
    print("Name:", match.group(1), match.group(2))  
    print("Age:", match.group(3))  
else:  
    print("Match not found.")

```  
Explanation -

In the above example, we use regex to extract the name and age from a string that has a specific format. The pattern 
```r"(\w+) (\w+) \((\d+) years old\)"``` matches a first name, last name, and age in parentheses. We use the match.group()
method to extract the matched groups and print them.


## 8. Easy Way to Remove String
Generally, we use the loop to reverse the given string; it can be also reversed using slicing. However, it is not a Pythonic way.
Let's see the following example.

### Example -
```

name = "Peter"  
print(name[::-1])

``` 
### Output -
```

reteP

```
