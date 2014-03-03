from vector import MyVector
from physics import Physics

class Entity:
	def __init__(self, name, mesh = "", pos = MyVector(0,0,0), vel = MyVector(0,0,0), yaw = 0):
		self.name = name
		self.pos = pos
		self.vel = vel
		self.mesh = mesh
		self.yaw = yaw
		self.aspectTypes = [Physics] 
		self.aspects = [Physics(self)]

	def tick(self, time):
		self.aspects[0].tick(time)

	def __str__(self):
		posString = "{" + str(self.pos.a) + ", " + str(self.pos.b) + ", " + str(self.pos.c) + "}"
		velString = "{" + str(self.vel.a) + ", " + str(self.vel.b) + ", " + str(self.vel.c) + "}"
		retString = "Name:"+self.name+" Pos:"+posString+" Vel:"+velString+" Yaw:"+str(self.yaw)
		return retString

