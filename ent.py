from vector import MyVector
from physics import Physics

class Entity:
	def __init__(self, name, mesh = "", pos = MyVector(0,0,0), vel = MyVector(0,0,0), yaw = 0, aspectTypes = [], aspects = []):
		self.name = name
		self.pos = pos
		self.vel = vel
		self.mesh = mesh
		self.yaw = yaw
		self.aspectTypes = aspectTypes 
		self.aspects = aspects

	def tick(self, time):
		#print self.pos.a, self.pos.b, self.pos.c, self.vel.a, self.vel.b, self.vel.c
		self.pos = self.pos + (self.vel * time)
		print self.pos.a, self.pos.b, self.pos.c, self.vel.a, self.vel.b, self.vel.c
		var = raw_input('asdf')
		#print self.pos.a + self.vel.a * 0.80
		#print time, self.pos.a, self.pos.b, self.pos.c

	def __str__(self):
		posString = "{" + str(self.pos.a) + ", " + str(self.pos.b) + ", " + str(self.pos.c) + "}"
		velString = "{" + str(self.vel.a) + ", " + str(self.vel.b) + ", " + str(self.vel.c) + "}"
		retString = posString + velString # "Name:"+self.name+" Mesh:"+self.mesh+" Pos:"+posString+" Vel:"+velString+" Yaw:"+str(self.yaw)
		return retString
