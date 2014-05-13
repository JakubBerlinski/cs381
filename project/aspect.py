import ogre.renderer.OGRE as ogre
from math import sin, cos, radians
import math, ai
import ent as ents

def fixAngle(angle):
    while angle > math.pi:
        angle -= 2.0 * math.pi
    while angle < -math.pi:
        angle += 2.0 * math.pi

    return angle

def diffAngle(angle1, angle2):
    return fixAngle(angle1 - angle2)


def clamp(val, min, max):
    if val <= min:
        return min
    elif val >= max:
        return max

    return val


class Physics(object):
    '''Class for handling physics on an entity'''
    def __init__(self, entity):
        self.entity = entity
        
    def tick(self,dt):
        ent = self.entity
        vel = ent.vel
        #orientation = ent.orientation #ogre.Vector3(cos(ent.heading), 0, sin(ent.heading))
        
        if isinstance(ent, ents.MISSILE):
            ent.orientation = ent.quaternion.xAxis() + ent.quaternion.yAxis() + ent.quaternion.zAxis()
            
        orientation = ent.orientation
        # if ent.speed < ent.maxSpeed:
        #     ent.speed += ent.acceleration * dt

        # elif ent.speed > ent.maxSpeed:
        #     ent.speed -= ent.acceleration * dt

        # timeScaledRotation = ent.turningRate * dt
        # angleDiff = diffAngle(ent.desiredHeading, ent.heading)
        # dheading = clamp(angleDiff, -timeScaledRotation, timeScaledRotation)

        # ent.heading += dheading
        up = ent.engine.inputMgr.camera.getUp()
        cross = up.crossProduct(orientation)
        vel.x = ent.speed * orientation.x + (cross.x * ent.sideSpeed)#+ ((orientation.x - math.pi/2.0) * ent.leftSpeed) + ((orientation.x - math.pi/2.0) * ent.rightSpeed)
        vel.y = ent.speed * orientation.y + ent.upSpeed
        vel.z = ent.speed * orientation.z  + (cross.z * ent.sideSpeed)#+ ((orientation.z - math.pi/2.0) * ent.leftSpeed) + ((orientation.z - math.pi/2.0) * ent.rightSpeed)
        
        ent.pos = ent.pos + vel * dt
        #print ent.pos

    def __str__(self):
        return 'Physics Aspect'
        
    def __repr__(self):
        return self.__str__()

class Renderable(object):
    ''' Class for rendering entities'''
    def __init__(self, entity):
        self.entity = entity
        if self.entity.uiname == "WALL":
            entity.node.setMaterialName('Examples/Rockwall')

    def tick(self,dt):
        node = self.entity.node
        node.setPosition(self.entity.pos)
        #node.resetOrientation()
        if self.entity.quaternion != ogre.Quaternion(0,0,0,0):
            node.setOrientation(self.entity.quaternion)
            
        if self.entity == self.entity.engine.gameMgr.player_ent:
            self.entity.quaternion = self.entity.engine.inputMgr.camera.getDerivedOrientation()



class UnitAI(object):
    def __init__(self, entity):
        self.entity = entity

    def tick(self, dt):
        commands = self.entity.commands

        if commands != []:
            commands[0].tick(dt)

