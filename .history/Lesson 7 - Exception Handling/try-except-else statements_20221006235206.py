# try-except-else Statements
# We can also use the else statement with the try-except statement in which, we can
# place the code which will be executed in the scenario if no exception occurs in the
# else block.
try:
    c = 2/1
except Exception as e:
    print("can't divide by zero")
    print(e)
else:
    print("Hi I am else block")
    
# Output: Hi I am else block

# We get this output because there is no exception in the try block and hence the else
# block is executed. If there was an exception in the try block, the else block will be
# skipped and except block will be executed

# The try statement in Python can have an optional finally clause. This clause is
# executed no matter what and is generally used to release external resources.
# Here is an example of file operations to illustrate this:

try:
    f = open("test.txt",encoding = 'utf-8')
 # perform file operations
finally:
 f.close()