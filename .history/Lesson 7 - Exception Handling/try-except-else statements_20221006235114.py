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
    
#