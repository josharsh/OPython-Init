name = input("Enter name: ")

if name.lower() < "c":
    print("less than")
else:
    print("greater than")

def is_palindrome(s: str) -> bool:
    """
    Determine whether the string is palindrome
    :param s:
    :return: Boolean
    >>> is_palindrome("a man a plan a canal panama".replace(" ", ""))
    True
    >>> is_palindrome("Hello")
    False
    >>> is_palindrome("Able was I ere I saw Elba")
    True
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("Mr. Owl ate my metal worm?")
    True
    """
    # Since Punctuation, capitalization, and spaces are usually ignored while checking
    # Palindrome,  we first remove them from our string.
    s = "".join([character for character in s.lower() if character.isalnum()])
    return s == s[::-1]



s = input("Enter string to determine whether its palindrome or not: ").strip()
if is_palindrome(s):
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")
