# Entity class to hold information about entities for 38Engine
# Sushil Louis

import ogre.renderer.OGRE as ogre
from physics import Physics
from render  import Renderable
class Entity:
    aspectTypes = [Physics, Renderable]
    
    def __init__(self, id, sceneManager, nodeId, pos = ogre.Vector3(0,0,0), mesh = 'robot.mesh', vel = ogre.Vector3(0, 0, 0), yaw = 0):
        self.id = id
        self.sceneManager = sceneManager
        self.pos = pos
        self.vel = vel
        self.mesh = mesh
        self.node = None
        self.deltaSpeed = 5
        self.deltaYaw   = 0.8
        self.speed = 0.0
        self.heading = 0.0
        self.aspects = []
        self.uid = nodeId
        self.initAspects()

        
    def initAspects(self):
        for aspType in self.aspectTypes:
            self.aspects.append(aspType(self,self.sceneManager, self.uid))
        
    def tick(self, dtime):
        for aspect in self.aspects:
            aspect.tick(dtime)

    def __str__(self):
        x = "Entity: %s \nPos: %s, Vel: %s,  mesh = %s\nSpeed: %f, Heading: %f" % (self.id, str(self.pos), str(self.vel), self.mesh, self.speed, self.heading)
        return x


class CVN68(Entity):
    def __init__(self, id, sceneManager, nid, pos = ogre.Vector3(0,0,0), vel = ogre.Vector3(0, 0, 0), yaw = 0):
        self.uiname = 'CVN68'
        self.mesh = 'cvn68.mesh'
        Entity.__init__(self, id, sceneManager, nid, mesh = self.mesh, pos = pos, vel = vel, yaw = yaw)
        self.acceleration = 2
        self.turningRate  = 0.01
        self.maxSpeed = 10
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0


class CIGARETTE(Entity):
    def __init__(self, id, sceneManager, nid, pos = ogre.Vector3(0,0,0), vel = ogre.Vector3(0, 0, 0), yaw = 0):
        self.uiname = 'CIGARETTE'
        self.mesh = 'cigarette.mesh'
        Entity.__init__(self, id, sceneManager, nid, mesh = self.mesh, pos = pos, vel = vel, yaw = yaw)
        self.acceleration  = 6
        self.turningRate   = 0.1
        self.maxSpeed = 40
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0

class MONTEREY(Entity):
    def __init__(self, id, sceneManager, nid, pos = ogre.Vector3(0,0,0), vel = ogre.Vector3(0, 0, 0), yaw = 0):
        self.uiname = 'MONTEREY'
        self.mesh = '3699_Monterey_189_92.mesh'
        Entity.__init__(self, id, sceneManager, nid, mesh = self.mesh, pos = pos, vel = vel, yaw = yaw)
        self.acceleration = 5
        self.turningRate = 0.1
        self.maxSpeed = 35
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0

class JETSKI(Entity):
    def __init__(self, id, sceneManager, nid, pos = ogre.Vector3(0,0,0), vel = ogre.Vector3(0, 0, 0), yaw = 0):
        self.uiname = 'JETSKI'
        self.mesh = '4685_Personal_Watercr.mesh'
        Entity.__init__(self, id, sceneManager, nid, mesh = self.mesh, pos = pos, vel = vel, yaw = yaw)
        self.acceleration = 7
        self.turningRate = 0.15
        self.maxSpeed = 20
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0

class SAILBOAT(Entity):
    def __init__(self, id, sceneManager, nid, pos = ogre.Vector3(0,0,0), vel = ogre.Vector3(0, 0, 0), yaw = 0):
        self.uiname = 'SAILBOAT'
        self.mesh = 'sailboat.mesh'
        Entity.__init__(self, id, sceneManager, nid, mesh = self.mesh, pos = pos, vel = vel, yaw = yaw)
        self.acceleration = 3
        self.turningRate = 0.1
        self.maxSpeed = 10
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0

class SLEEK(Entity):
    def __init__(self, id, sceneManager, nid, pos = ogre.Vector3(0,0,0), vel = ogre.Vector3(0, 0, 0), yaw = 0):
        self.uiname = 'SLEEK'
        self.mesh = 'sleek.mesh'
        Entity.__init__(self, id, sceneManager, nid, mesh = self.mesh, pos = pos, vel = vel, yaw = yaw)
        self.acceleration = 4
        self.turningRate = 0.02
        self.maxSpeed = 30
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0

class BOAT(Entity):
    def __init__(self, id, sceneManager, nid, pos = ogre.Vector3(0,0,0), vel = ogre.Vector3(0, 0, 0), yaw = 0):
        self.uiname = 'BOAT'
        self.mesh = 'boat.mesh'
        Entity.__init__(self, id, sceneManager, nid, mesh = self.mesh, pos = pos, vel = vel, yaw = yaw)
        self.acceleration = 5
        self.turningRate = 0.1
        self.maxSpeed = 30
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0

class DDG51(Entity):
    def __init__(self, id, sceneManager, nid, pos = ogre.Vector3(0,0,0), vel = ogre.Vector3(0, 0, 0), yaw = 0):
        self.uiname = 'DDG51'
        self.mesh = 'ddg51.mesh'
        Entity.__init__(self, id, sceneManager, nid, mesh=self.mesh, pos = pos, vel = vel, yaw = yaw)
        self.acceleration = 5
        self.turningRate = 0.02
        self.maxSpeed = 32
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0

class ALIENSHIP(Entity):
    def __init__(self, id, sceneManager, nid, pos = ogre.Vector3(0,0,0), vel = ogre.Vector3(0, 0, 0), yaw = 0):
        self.uiname = 'ALIEN'
        self.mesh = 'alienship.mesh'
        Entity.__init__(self, id, sceneManager, nid, mesh = self.mesh, pos = pos, vel = vel, yaw = yaw)
        self.acceleration  = 10
        self.turningRate   = 0.3
        self.maxSpeed = 60
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0

class BOAT2(Entity):
    def __init__(self, id, sceneManager, nid, pos = ogre.Vector3(0,0,0), vel = ogre.Vector3(0, 0, 0), yaw = 0):
        self.uiname = 'BOAT2'
        self.mesh = '5086_Boat.mesh'
        Entity.__init__(self, id, sceneManager, nid, mesh = self.mesh, pos = pos, vel = vel, yaw = yaw)
        self.acceleration = 5
        self.turningRate = 0.025
        self.maxSpeed = 30
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0

