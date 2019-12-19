import math

class Point(object):
	"""simple class Point"""
	def __init__(self, x, y):
		"""pass x, y coordinates to build a 2d point"""
		self.x = x
		self.y = y

	def dist(self, p):
		"""return distance between to another point (p)"""
		return math.sqrt(math.pow((p.x - self.x), 2) + math.pow((p.y - self.y), 2))

	def minus(self, p):
		"""return a new point that's equal to actual point minus a point p"""
		return Point(self.x - p.x, self.y - p.y)
	
	def plus(self, p):
		"""return a new point that's equal to actual point plus a point p"""
		return Point(self.x + p.x, self.y + p.y)

	def info(self):
		"""show info about the point"""
		print('({}, {})'.format(self.x, self.y))

class Polygon(object):
	"""this class is a simple polygon, in other words, a list of points"""
	def __init__(self, points):
		self.points = points

	"""show polygon about the polygon"""
	def info(self):
		for p in self.points:
			p.info()

if __name__ == '__main__':
	# create two points p1, p2
	p1 = Point(3, 4)
	p2 = Point(7, 2)

	p1.info()
	p2.info()

	# create a new point p3 = p1 - p2
	p3 = p1.minus(p2)
	p3.info()

	# create a new point p4 = p1 + p2
	p4 = p1.plus(p2)
	p4.info()

	# show distance between p3 and p4
	print(p3.dist(p4))

	# create a polygon passing a list with the previous points as parameter
	polygon = Polygon(list([p1, p2, p3, p4]))

	# show polygon info
	polygon.info()

		