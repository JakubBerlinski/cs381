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
		if(type == 'speedboat'):
			self.entityList.append(SpeedboatEntity(sceneManager, str(self.uniqueId), mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, turningRate))
		if(type == 'scout'):
			self.entityList.append(ScoutEntity(sceneManager, str(self.uniqueId), mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, turningRate))
		if(type == 'superspeedboat'):
			self.entityList.append(SuperspeedboatEntity(sceneManager, str(self.uniqueId), mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, turningRate))
		if(type == 'alienship'):
			self.entityList.append(AlienshipEntity(sceneManager, str(self.uniqueId), mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, turningRate))
		if(type == 'aircraftcarrier'):
			self.entityList.append(AircraftCarrierEntity(sceneManager, str(self.uniqueId), mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, turningRate))
		if(type == 'gunship'):
			self.entityList.append(GunshipEntity(sceneManager, str(self.uniqueId), mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, turningRate))

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

		elif(direction == 4):
			self.entityList[self.selectedEntity].vel = ogre.Vector3(0,0,0)
			self.entityList[self.selectedEntity].speed = 0
			self.entityList[self.selectedEntity].desiredSpeed = 0

	def updateSelection(self):
		node = self.sceneManager.getSceneNode(self.entityList[self.selectedEntity].name)
		node.showBoundingBox(False)
		self.selectedEntity += 1
		if(self.selectedEntity >= len(self.entityList)):
			self.selectedEntity = 0

		node = self.sceneManager.getSceneNode(self.entityList[self.selectedEntity].name)
		node.showBoundingBox(True)

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
		self.maxSpeed = 6
		self.turningRate = 10.0
		self.acceleration = 2
		Entity.__init__(self, sceneManager, name, mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, self.turningRate)

class DestroyerEntity(Entity):
	def __init__(self, sceneManager, name, mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, turningRate):
		self.maxSpeed = 40
		self.turningRate = 2
		self.acceleration = 3
		Entity.__init__(self, sceneManager, name, mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, self.turningRate)

class SpeedboatEntity(Entity):
	def __init__(self, sceneManager, name, mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, turningRate):
		self.maxSpeed = 30
		self.turningRate = 8
		self.acceleration = 7
		Entity.__init__(self, sceneManager, name, mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, self.turningRate)

class ScoutEntity(Entity):
	def __init__(self, sceneManager, name, mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, turningRate):
		self.maxSpeed = 25
		self.turningRate = 3
		self.acceleration = 4
		Entity.__init__(self, sceneManager, name, mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, self.turningRate)

class SuperspeedboatEntity(Entity):
	def __init__(self, sceneManager, name, mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, turningRate):
		self.maxSpeed = 35
		self.turningRate = 10
		self.acceleration = 8
		Entity.__init__(self, sceneManager, name, mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, self.turningRate)

class AlienshipEntity(Entity):
	def __init__(self, sceneManager, name, mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, turningRate):
		self.maxSpeed = 150
		self.turningRate = 50
		self.acceleration = 25
		Entity.__init__(self, sceneManager, name, mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, self.turningRate)

class AircraftCarrierEntity(Entity):
	def __init__(self, sceneManager, name, mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, turningRate):
		self.maxSpeed = 60
		self.turningRate = 0.5
		self.acceleration = 2
		Entity.__init__(self, sceneManager, name, mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, self.turningRate)

class GunshipEntity(Entity):
	def __init__(self, sceneManager, name, mesh, pos, vel, heading, speed, desiredSpeed, desiredHeading, turningRate):
		self.maxSpeed = 40
		self.turningRate = 2.5
		self.acceleration = 3.0
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
