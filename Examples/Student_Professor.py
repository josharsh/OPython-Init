#Anuneet Anand

'''
A sample code to show Object Oriented Programming in Python. 
Two class definitions are given : Student Class & Professor Class
Student Class has attributes - Roll Number , Name , Group (Red/Blue)
Professor Class has attributes - Name , Subject , List Of Student Objects
Three objects of student class are instantiated in main() and are assigned to a professor which is also instantiated in main().
Another student object is instantiated and it's equality is tested, followed by modification of it's data attributes through Setters.
Print Details Function of both the classes are called in main()	
'''

#Information about a student.
class Student:

	# Constructor
	def __init__(self,Roll_Number,Name,Group):
     """
     Initialize a new instance.

     Args:
         self: (todo): write your description
         Roll_Number: (int): write your description
         Name: (str): write your description
         Group: (todo): write your description
     """
		self.Roll_Number = Roll_Number
		self.Name = Name
		self.Group = Group

	# Equals Method : To check if two objects of this class are equal.
	def __eq__(self, other):
     """
     Compares two values are equal values.

     Args:
         self: (todo): write your description
         other: (todo): write your description
     """
		if isinstance(other, self.__class__):
			return (self.Roll_Number == other.Roll_Number) and (self.Name == other.Name) and (self.Group == other.Group)
		else:
			return False

	#SETTERS
	def set_Group(self,New_Group):
     """
     Set the group group of the group

     Args:
         self: (todo): write your description
         New_Group: (todo): write your description
     """
		self.Group = New_Group
	
	#GETTERS
	def get_Roll_Number(self):
     """
     : returns : class

     Args:
         self: (todo): write your description
     """
		return self.Roll_Number
	def get_Name(self):
     """
     Returns the name of the name

     Args:
         self: (todo): write your description
     """
		return self.Name
	def get_Group(self):
     """
     Return the group of the group

     Args:
         self: (todo): write your description
     """
		return self.Group

	# Print Method : To print the data attributes of the class.
	def Print_Details(self):
     """
     Prints the details of the group.

     Args:
         self: (todo): write your description
     """
		print(">--- Student Details ---<")
		print("Roll Number:",self.Roll_Number)
		print("Name:",self.Name)
		print("Group:",self.Group)

#Information about a professor.
class Professor:

	# Constructor
	def __init__(self,Name,Subject):
     """
     Initialize a new instance

     Args:
         self: (todo): write your description
         Name: (str): write your description
         Subject: (str): write your description
     """
		self.Name = Name
		self.Subject = Subject
		self.Students = []

	#SETTERS
	def set_Students(self,Students_List):
     """
     : parameter_List.

     Args:
         self: (todo): write your description
         Students_List: (list): write your description
     """
		self.Students = Students_List

	#GETTERS
	def get_Name(self):
     """
     Returns the name of the name

     Args:
         self: (todo): write your description
     """
		return self.Name
	def get_Subject(self):
     """
     : return : class

     Args:
         self: (todo): write your description
     """
		return self.Subject
	def get_Students(self):
     """
     Returns the next : class : class :.

     Args:
         self: (todo): write your description
     """
		return self.Students

	# Print Method : To print the data attributes of the class.
	def Print_Details(self):
     """
     Prints the details of the database.

     Args:
         self: (todo): write your description
     """
		print(">--- Professor Details ---<")
		print("Name:",self.Name)
		print("Subject:",self.Subject)
		print("NUmber Of Students:",len(self.Students))


if __name__ == '__main__':
	P = Professor("Samuel","Physics")
	S1 = Student(1,"Andy","Red")
	S2 = Student(2,"Jack","Blue")
	S3 = Student(3,"Sam","Blue")
	SX = Student(2,"Jack","Red")		# Extra Student
	L = [S1,S2,S3]						# List Of Students
	P.set_Students(L)

	if (S2==SX):						# Testing Equality
		S2.Print_Details()				# Fails : Red in SX but Blue in S2
	else:
		print("Not Equal")

	SX.set_Group("Blue")				# Modifying Data Attribute 

	if (S2==SX):						# Testing Equality
		S2.Print_Details()				# Passes :- Printing Details Of S2
	else:
		print("Not Equal")

	P.Print_Details()					# Printing Details Of Professor

#END OF CODE

