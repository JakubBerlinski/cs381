from vector import MyVector
from physics import Physics

class Entity:
	def __init__(self, mesh = "", pos = MyVector(0,0,0), vel = MyVector(0,0,0), yaw = 0, aspectTypes = [], aspects = []):
		self.pos = pos
		self.vel = vel
		self.mesh = mesh
		self.yaw = yaw
		self.aspectTypes = aspectTypes 
		self.aspects = aspects

	def tick(self, time):
		self.pos = self.pos + (self.vel * time)	
