
from aspect import Physics, Renderable, UnitAI
import math

from ogre.renderer.OGRE import Vector3, Quaternion
class Entity(object):
    aspectTypes = [Physics, Renderable, UnitAI]

    def __init__(self, engine, id, pos = Vector3(0,0,0), mesh = 'robot.mesh', vel = Vector3(0, 0, 0), yaw = 0, orientation = Vector3().ZERO):
        self.engine = engine
        self.ogreName = str(id)
        self.id = id
        self.pos = pos
        self.vel = vel
        self.mesh = mesh
        self.node = None
        self.speed = 0
        self.heading = float(yaw)
        self.pitch = 0.0
        self.commands = []
        self.aspects = []
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.sideSpeed = 0
        self.upSpeed = 0
        self.orientation = Vector3().ZERO
        self.upVec = Vector3().ZERO
        self.scale = 1.0
        self.material = 'BorgCube'
        self.health = 5
        self.quaternion = Quaternion(0,0,0,0)


    def initAspects(self):
        for aspType in self.aspectTypes:
            self.aspects.append(aspType(self))


    def tick(self, dtime):
        for aspect in self.aspects:
            aspect.tick(dtime)
            
    def __eq__(self, other):
        return self.id == other.id


    def __str__(self):
        x = "Entity: %s \nPos: %s, Vel: %s,  mesh = %s\nSpeed: %f, Heading: %f" % (self.id, str(self.pos), str(self.vel), self.mesh, self.speed, self.heading)
        return x

class DRONE(Entity):
    def __init__(self, engine, id, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), yaw = 0, orientation = Vector3().ZERO):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'drone.mesh'
        self.uiname = 'DRONE'
        self.material = 'Drone/Orange'
        self.acceleration = 2
        self.turningRate  = 0.01
        self.maxSpeed = 50
        #self.speed = 0
        self.heading = float(yaw)
        self.health = 5
        self.shot = False

    def tick(self, dt):
        Entity.tick(self,dt)

        if self.pos.x > 92.0:
            self.pos.x -= 1.0

        elif self.pos.x < -92.0:
            self.pos.x += 1.0

        if self.pos.z > 92.0:
            self.pos.z -= 1.0

        elif self.pos.z < -92.0:
            self.pos.z += 1.0

        if self.pos.y > 123.0:
            self.pos.y -= 1.0

        elif self.pos.y < 6.0:
            self.pos.y += 1.0

        if math.sqrt((3.6 - self.pos.x) * (3.6 - self.pos.x) + (0.5 - self.pos.z) * (0.5 - self.pos.z)) < (3 + 20):
            self.pos = self.pos - self.vel * dt

        if math.sqrt((-60 - self.pos.x) * (-60 - self.pos.x) + (-65 - self.pos.z) * (-65 - self.pos.z)) < (3 + 20):
            self.pos = self.pos - self.vel * dt

        if math.sqrt((70 - self.pos.x) * (70 - self.pos.x) + (-65 - self.pos.z) * (-65 - self.pos.z)) < (3 + 20):
            self.pos = self.pos - self.vel * dt

        if math.sqrt((70 - self.pos.x) * (70 - self.pos.x) + (65 - self.pos.z) * (65 - self.pos.z)) < (3 + 20):
            self.pos = self.pos - self.vel * dt

        if math.sqrt((-60 - self.pos.x) * (-60 - self.pos.x) + (65 - self.pos.z) * (65 - self.pos.z)) < (3 + 20):
            self.pos = self.pos - self.vel * dt



class WALL(Entity):
    def __init__(self, engine, id, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), yaw = 0, orientation = Vector3().ZERO):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'wall.mesh'
        self.uiname = 'WALL'
        self.acceleration = 0
        self.turningRate  = 0
        self.maxSpeed = 0
        #self.speed = 0
        self.heading = float(yaw)

class BULLET(Entity):
    def __init__(self, engine, id, pos = Vector3().ZERO, vel = Vector3().ZERO, orientation = Vector3().ZERO, yaw = 0):
        Entity.__init__(self, engine, id, pos, vel = vel)
        self.mesh = 'sphere.mesh'
        self.uiname = 'BULLET'
        self.speed = self.maxSpeed = 200
        self.orientation = orientation
        self.scale = 0.001
        self.aliveTime = 0.0
        self.material = 'Snow'

    def tick(self, dt):
        Entity.tick(self,dt)
        self.aliveTime += dt
        destroyed = False

        if self.aliveTime > 3.0:
            self.engine.entityMgr.deleteEnt.append(self)
            destroyed = True

        distance = self.pos.distance(self.engine.gameMgr.enemy_ent.pos)
        distance2 = self.pos.distance(self.engine.gameMgr.player_ent.pos)
        
        if distance < 3.0 and self.aliveTime > 0.1:
            self.engine.gameMgr.enemy_ent.health -= 1
            print "Hit: Enemy Health:", self.engine.gameMgr.enemy_ent.health
            
            if not destroyed:
                self.engine.entityMgr.deleteEnt.append(self)
        '''
        if distance2 < 3.0 and self.aliveTime > 0.1:
            self.engine.gameMgr.player_ent.health -= 1
            print "Hit: Player Health:", self.engine.gameMgr.player_ent.health

            if not destroyed:
                self.engine.entityMgr.deleteEnt.append(self)

            return
        '''

class MISSILE(Entity):
    def __init__(self, engine, id, pos = Vector3().ZERO, vel = Vector3().ZERO, orientation = Vector3().ZERO, yaw = 0):
        Entity.__init__(self, engine, id, pos, vel = vel)
        self.mesh = 'sphere.mesh'
        self.uiname = 'MISSILE'
        self.speed = self.maxSpeed = 30
        self.orientation = orientation
        self.scale = 0.01
        self.aliveTime = 0.0

    def tick(self, dt):
        Entity.tick(self,dt)
        self.aliveTime += dt
        destroyed = False

        if self.aliveTime > 6.0:
            self.engine.entityMgr.deleteEnt.append(self)
            destroyed = True
            
        if self.pos.x > 92.0:
            self.engine.entityMgr.deleteEnt.append(self)
            destroyed = True

        elif self.pos.x < -92.0:
            self.engine.entityMgr.deleteEnt.append(self)
            destroyed = True

        if self.pos.z > 92.0:
            self.engine.entityMgr.deleteEnt.append(self)
            destroyed = True

        elif self.pos.z < -92.0:
            self.engine.entityMgr.deleteEnt.append(self)
            destroyed = True

        if self.pos.y > 123.0:
            self.engine.entityMgr.deleteEnt.append(self)
            destroyed = True

        elif self.pos.y < 6.0:
            self.engine.entityMgr.deleteEnt.append(self)
            destroyed = True

        if math.sqrt((3.6 - self.pos.x) * (3.6 - self.pos.x) + (0.5 - self.pos.z) * (0.5 - self.pos.z)) < (3 + 20):
            self.engine.entityMgr.deleteEnt.append(self)
            destroyed = True

        if math.sqrt((-60 - self.pos.x) * (-60 - self.pos.x) + (-65 - self.pos.z) * (-65 - self.pos.z)) < (3 + 20):
            self.engine.entityMgr.deleteEnt.append(self)
            destroyed = True

        if math.sqrt((70 - self.pos.x) * (70 - self.pos.x) + (-65 - self.pos.z) * (-65 - self.pos.z)) < (3 + 20):
            self.engine.entityMgr.deleteEnt.append(self)
            destroyed = True

        if math.sqrt((70 - self.pos.x) * (70 - self.pos.x) + (65 - self.pos.z) * (65 - self.pos.z)) < (3 + 20):
            self.engine.entityMgr.deleteEnt.append(self)
            destroyed = True

        if math.sqrt((-60 - self.pos.x) * (-60 - self.pos.x) + (65 - self.pos.z) * (65 - self.pos.z)) < (3 + 20):
            self.engine.entityMgr.deleteEnt.append(self)
            destroyed = True
            
        distance = self.pos.distance(self.engine.gameMgr.enemy_ent.pos)
        distance2 = self.pos.distance(self.engine.gameMgr.player_ent.pos)
        
        if distance < 3.0 and self.aliveTime > 0.2:
            self.engine.gameMgr.enemy_ent.health -= 1
            print "Hit: Enemy Health:", self.engine.gameMgr.enemy_ent.health
            
            self.engine.soundMgr.play('blast')

            if not destroyed:
                self.engine.entityMgr.deleteEnt.append(self)
        '''       
        if distance2 < 3.0 and self.aliveTime > 0.1:
            self.engine.gameMgr.player_ent.health -= 1
            print "Hit: Player Health:", self.engine.gameMgr.player_ent.health

            if not destroyed:
                self.engine.entityMgr.deleteEnt.append(self)
        '''

