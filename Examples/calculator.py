'''
    A simple calculator using oop in python
'''

# A calculator class
class Calc():
    
    # functions to define our operators (+,-,*,/)
    @staticmethod
    def add(x, y):
        """
        Add a new point to the graph

        Args:
            x: (int): write your description
            y: (int): write your description
        """
        return x + y
        
    @staticmethod
    def sub(x, y):
        """
        Subsub ( x y ) of y.

        Args:
            x: (int): write your description
            y: (int): write your description
        """
        return x - y

    @staticmethod
    def mul(x, y):
        """
        Returns the x y and return the value of x

        Args:
            x: (array): write your description
            y: (array): write your description
        """
       return x * y
       
    @staticmethod
    def div(x, y):
        """
        Divide a vector x and y.

        Args:
            x: (int): write your description
            y: (int): write your description
        """
        return x / y

    # Define a function to get our integer inputs   
    @staticmethod
    def get_numbers():
        """
        Returns a list of numbers

        Args:
        """
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        return num1, num2

    # Define a function to get the operator which will determine the operation to carry out on the inputed integers
    @staticmethod
    def get_operator():
        """
        Returns the operator operator

        Args:
        """
        operator = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
        return operator

    # Define our function to perform the operation
    @classmethod
    def calculate(cls):
        """
        Calculate the total number.

        Args:
            cls: (todo): write your description
        """
        num1, num2 = cls.get_numbers()
        operator = cls.get_operator()
        if operator == '+':
            print (cls.add(num1, num2))
        elif operator == '-':
            print (cls.sub(num1, num2))
        elif operator == '*':
            print (cls.mul(num1, num2))
        elif operator == '/':
            print (cls.div(num1, num2))
        else:
            print('You have not typed a valid operator, please run the program again.')

        Calc.again()

    # Define again() function to ask user if they want to use the calculator again
    @classmethod
    def again(cls):
        """
        Calculate the database

        Args:
            cls: (todo): write your description
        """

        # Take input from user
        calc_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''')

        # If user types Y, run the calculate() function
        if calc_again.upper() == 'Y':
            Calc.calculate()

        # If user types N, say good-bye to the user and end the program
        elif calc_again.upper() == 'N':
            print('See you later.')

        # If user types another key, run the function again
        else:
            Calc.again()

# Call calculate() outside of the function
Calc.calculate()