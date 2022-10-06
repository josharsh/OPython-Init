
# a=10/0
# print(a)

# ---------------------------------------------------------------------------
# ZeroDivisionError                         Traceback (most recent call last)
# <ipython-input-3-fcc871b1b29d> in <module>
# ----> 1 a=10/0
#       2 a

# ZeroDivisionError: division by zero

# a = b*4
# # print(a)
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-4-d73acdbee43e> in <module>
# ----> 1 a = b*4
#       2 a

# NameError: name 'b' is not defined
# a = 'b'+4
# a
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-6-f5b8a2ff08cc> in <module>
# ----> 1 a = 'b'+4
#       2 a

# TypeError: can only concatenate str (not "int") to str
# a = int(input('enter value of a'))
# b = int(input('enter value of b'))
# c = a/b
# c
# enter value of a12
# enter value of babc
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-9-fb1c95fad195> in <module>
#       1 a = int(input('enter value of a'))
# ----> 2 b = int(input('enter value of b'))
#       3 c = a/b
#       4 c

# ValueError: invalid literal for int() with base 10: 'abc'

try:   
    A = int(input('ENTER THE VALUE:'))
    B = int(input('ENTER THE VALUE:'))
    print(A/B)
except:
    print('A & B SHOULD BE INTEGER')
# ENTER THE VALUE:56
# ENTER THE VALUE:gn
# A & B SHOULD BE INTEGER
while True:
    try:   
        A = int(input('ENTER THE VALUE:'))
        B = int(input('ENTER THE VALUE:'))
        print(A/B)
        break
    except ValueError:
        print('A & B SHOULD BE INTEGER')
        
while True:    
    try:   
        A = int(input('ENTER THE VALUE:'))
        B = int(input('ENTER THE VALUE:'))
        print(A/B)
        break
    except ValueError:
        print('A & B SHOULD BE INTEGER')
    except ZeroDivisionError:
        print('B SHOULD NOT BE ZERO')