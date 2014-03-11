from math import cos, sin, radians
import ogre.renderer.OGRE as ogre

class Physics:
	def __init__(self, entity):
		self.entity = entity

	def tick(self, time):
		PI = 3.1415
		orientation = ogre.Vector3(cos(radians(self.entity.heading)), 0, sin(radians(self.entity.heading)))

		if(self.entity.speed <= self.entity.maxSpeed and self.entity.speed >= -self.entity.maxSpeed):
			if(self.entity.speed < self.entity.desiredSpeed):
				self.entity.speed += self.entity.acceleration * time
			elif(self.entity.speed > self.entity.desiredSpeed):
				self.entity.speed -= self.entity.acceleration * time

		if(self.entity.heading != self.entity.desiredHeading):
			if(self.entity.heading > self.entity.desiredHeading):
				self.entity.heading -= self.entity.turningRate * time
			elif(self.entity.heading < self.entity.desiredHeading):
				self.entity.heading += self.entity.turningRate * time


		self.entity.vel.x = self.entity.speed * orientation.x
		self.entity.vel.z = self.entity.speed * orientation.z

		print self.entity.speed, self.entity.heading

		self.entity.pos = self.entity.pos + self.entity.vel * time

