# class ZeroDenominatorError(Exception):
#     pass
# while True:
#     try:
#         n = int(input())
#         m = int(input())
#         if m==0:
#             raise ZeroDenominatorError('Denominator should not be Zero')
#         print(n/m)
#         break
#     except ValueError:
#         print('A & B SHOULD BE INTEGER')
#     except ZeroDivisionError:
#         print('B SHOULD NOT BE ZERO')    
# 2
# 0
# ---------------------------------------------------------------------------
# ZeroDenominatorError                      Traceback (most recent call last)
# <ipython-input-2-662bc9ae2891> in <module>
#       6         m = int(input())
#       7         if m==0:
# ----> 8             raise ZeroDenominatorError('Denominator should not be Zero')
#       9         print(n/m)
#      10         break

# ZeroDenominatorError: Denominator should not be Zero
# class ZeroDenominatorError(Exception):
#     pass
# while True:
#     try:
#         n = int(input())
#         m = int(input())
#         if m==0:
#             raise ZeroDenominatorError('Denominator should not be Zero')
#         print(n/m)
#         break
#     except ValueError:
#         print('A & B SHOULD BE INTEGER')
#     except ZeroDivisionError:
#         print('B SHOULD NOT BE ZERO') 
# 2
# abc
# A & B SHOULD BE INTEGER
# 1
# 0
# ---------------------------------------------------------------------------
# ZeroDenominatorError                      Traceback (most recent call last)
# <ipython-input-4-73339e46993a> in <module>
#       6         m = int(input())
#       7         if m==0:
# ----> 8             raise ZeroDenominatorError('Denominator should not be Zero')
#       9         print(n/m)
#      10         break

# ZeroDenominatorError: Denominator should not be Zero

class ZeroDenominatorError(Exception):
    pass
while True:
    try:
        n = int(input())
        m = int(input())
        if m==0:
            raise ZeroDenominatorError('Denominator should not be Zero')
    except ValueError:
        print('A & B SHOULD BE INTEGER')
    except ZeroDivisionError:
        print('B SHOULD NOT BE ZERO') 
    else:
        print(n/m)
        break
# 2
# s
# A & B SHOULD BE INTEGER
# 2
# 2
# 1.0
class ZeroDenominatorError(Exception):
    pass
while True:
    try:
        n = int(input())
        m = int(input())
        if m==0:
            raise ZeroDenominatorError('Denominator should not be Zero')
    except ValueError:
        print('A & B SHOULD BE INTEGER')
    except ZeroDivisionError:
        print('B SHOULD NOT BE ZERO') 
    else:
        print(n/m)
        break
    finally:
        print('OUTPUT PRINTED')