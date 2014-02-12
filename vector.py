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

	def scalarMultiply(self,vec, scalar):
		ret = myVector(vec.a * scalar, vec.b * scalar, vec.c * scalar)
		return ret

	def scalarDivide(self, scalar):
		ret = myVector(vec.a / scalar, vec.b / scalar, vec.c / scalar)
		return ret

	def magnitude(self):
		return math.sqrt(self.a**2 + self.b**2 + self.c**2)

	def __add__(self, other):
		self.a = self.a+other.a
		self.b = self.b+other.b
		self.c = self.c+other.c
		return self

	def __sub__(self, other):
		self.a = self.a-other.a
		self.b = self.b-other.b
		self.c = self.c-other.c
		return self

	def __mul__(self, other):
		self.a = self.a*other
		self.b = self.b*other
		self.c = self.c*other
		return self

	def __rmul__(self, other):
		self.a = self.a*other
		self.b = self.b*other
		self.c = self.c*other
		return self

	def __div__(self, other):
		self.a = self.a/other
		self.b = self.b/other
		self.c = self.c/other
		return self
