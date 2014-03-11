import ogre.renderer.OGRE as ogre
from physics import Physics
from math import radians

class EntityMgr:
	def __init__(self, sceneManager):
		self.entityList = []
		self.uniqueId = 0
		self.selectedEntity = 0
		self.sceneManager = sceneManager

	def createEntity(self, sceneManager, type, mesh = "", pos = ogre.Vector3(0,0,0), vel = ogre.Vector3(0,0,0), heading = 0, speed = 0, desiredSpeed = 0, desiredHeading = 0, acceleration = ogre.Vector3(0,0,0), turningRate = 0):
		if(type == "sailboat"):
			self.entityList.append(SailboatEntity(sceneManager, str(self.uniqueId), mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, turningRate))
		if(type == 'destroyer'):
			self.entityList.append(DestroyerEntity(sceneManager, str(self.uniqueId), mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, turningRate))
		self.uniqueId += 1

	def updateEntities(self, time):
		for i in self.entityList:
			i.tick(time)

	def updateSelectedEntity(self, direction):
		if(direction == 0):
			self.entityList[self.selectedEntity].desiredSpeed -= 1

		elif(direction == 1):
			self.entityList[self.selectedEntity].desiredSpeed += 1

		elif(direction == 2):
			self.entityList[self.selectedEntity].desiredHeading -= 1

		elif(direction == 3):
			self.entityList[self.selectedEntity].desiredHeading += 1

	def updateSelection(self):
		self.selectedEntity += 1
		if(self.selectedEntity >= len(self.entityList)):
			self.selectedEntity = 0

class Entity:
	def __init__(self, sceneManager, name, mesh = "", pos = ogre.Vector3(0,0,0), vel = ogre.Vector3(0,0,0), heading = 0, speed = 0, desiredSpeed = 0, desiredHeading = 0, turningRate = 0):
		self.name = name
		self.mesh = mesh
		self.pos = pos
		self.vel = vel
		self.heading = heading
		self.speed = speed
		self.desiredSpeed = desiredSpeed
		self.desiredHeading = desiredHeading
		self.turningRate = turningRate
		self.sceneManager = sceneManager
		self.physics = Physics(self)
		self.renderable = Renderable(self, self.sceneManager)

	def tick(self, time):
		self.physics.tick(time)
		self.renderable.tick()

class SailboatEntity(Entity):
	def __init__(self, sceneManager, name, mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, turningRate):
		self.maxSpeed = 100.0
		self.turningRate = 10.0
		self.acceleration = 3.0
		Entity.__init__(self, sceneManager, name, mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, self.turningRate)

class DestroyerEntity(Entity):
	def __init__(self, sceneManager, name, mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, turningRate):
		self.maxSpeed = 150.0
		self.turningRate = 5.0
		self.acceleration = 6.0
		Entity.__init__(self, sceneManager, name, mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, self.turningRate)

class Renderable:
	def __init__(self, entity, sceneManager):
		self.entity = entity
		self.sceneManager = sceneManager
		self.ogreEntity = self.sceneManager.createEntity(self.entity.name, self.entity.mesh)
		node = self.sceneManager.getRootSceneNode().createChildSceneNode(self.entity.name)
		node.attachObject(self.ogreEntity)

		self.node = self.sceneManager.getSceneNode(self.entity.name)

	def tick(self):
		self.node.setPosition(self.entity.pos)
		self.node.setOrientation(ogre.Quaternion(radians(-self.entity.heading), ogre.Vector3(0,1,0)))