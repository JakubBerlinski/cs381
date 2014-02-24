import math

class MyVector:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def add(self, vec1, vec2):
		ret = myVector(vec1.a + vec2.a, vec1.b + vec2.b, vec1.c + vec2.c)
		return ret

	def sub(self, vec1, vec2):
		ret = myVector(vec1.a - vec2.a, vec1.b - vec2.b, vec1.c - vec2.c)
		return ret

	def scalarMultiply(self, vec, scalar):
		ret = myVector(vec.a * scalar, vec.b * scalar, vec.c * scalar)
		return ret

	def scalarDivide(self, scalar):
		ret = myVector(vec.a / scalar, vec.b / scalar, vec.c / scalar)
		return ret

	def magnitude(self):
		return math.sqrt(self.a**2 + self.b**2 + self.c**2)

	def __add__(self, other):
		return MyVector(self.a + other.a, self.b + other.b, self.c + other.c)

	def __sub__(self, other):
		return MyVector(self.a - other.a, self.b - other.b, self.c - other.c)

	def __mul__(self, other):
		return MyVector(self.a * other, self.b * other, self.c * other)

	def __div__(self, other):
		return MyVector(self.a / other.a, self.b / other.b, self.c / other.c)


