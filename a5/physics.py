# Simple ORIENTED Physics for 38Engine
# vel is rate of change of pos
# Sushil Louis

from vector import MyVector
import utils
import math

class Physics:
    def __init__(self, ent, sceneManager, uid):
        self.ent = ent
        self.uid = uid
        
    def tick(self, dtime):
        #----------position-----------------------------------
        timeScaledAcceleration = self.ent.acceleration * dtime
        self.ent.speed += utils.clamp( self.ent.desiredSpeed - self.ent.speed, -timeScaledAcceleration, timeScaledAcceleration)

        self.ent.vel.x = math.cos(-self.ent.heading) * self.ent.speed
        self.ent.vel.z = math.sin(-self.ent.heading) * self.ent.speed
        self.ent.vel.y = 0
        
        self.ent.pos = self.ent.pos + (self.ent.vel * dtime)

        #------------heading----------------------------------

        timeScaledRotation = self.ent.turningRate * dtime
        angleDiff = utils.diffAngle(self.ent.desiredHeading, self.ent.heading)
        dheading = utils.clamp(angleDiff, -timeScaledRotation, timeScaledRotation)

        self.ent.heading += dheading
