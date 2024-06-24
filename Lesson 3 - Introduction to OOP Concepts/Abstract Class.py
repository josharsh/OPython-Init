# ABSTRACT CLASS

# AN ABSTRACT CLASS CAN BE CONSIDERED AS A BLUEPRINT FOR OTHER CLASSES
# ALLOWS YOU TO CREATE SET OF METHODS.
# AN ABSTRACT METHOD IS A METHOD WHICH HAS DECLARATION BUT DOES NOT HAVE 
# ANY IMPLEMENTATION.

from abc import ABC, abstractmethod

class Polygon(ABC):
	# ABSTRACT METHOD
	def no_of_sides(self):
		pass

class Triangle(Polygon):
	# OVERRIDING ABSTRACT METHOD
	def no_of_sides(self):
		print("I HAVE 3 SIDES")

class Pentagon(Polygon):
	# OVERRIDING ABSTRACT METHOD
	def no_of_sides(self):
		print("I HAVE 5 SIDES")

class Hexagon(Polygon):
	# OVERRIDING ABSTRACT METHOD
	def no_of_sides(self):
		print("I HAVE 6 SIDES")

R = Triangle()
R.no_of_sides()

R = Pentagon()
R.no_of_sides()

R = Hexagon()
R.no_of_sides()
