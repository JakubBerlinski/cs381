import ogre.renderer.OGRE as ogre
import math

class Command(object):
    ''' Class for handling Command of an entity '''
    def __init__(self, entity, pos = ogre.Vector3(0,0,0)):
        self.entity = entity
        self.pos = pos

    def tick(self, dt):
        pass


class Intercept(Command):
    def __init__(self, entity, targetEnt):
        Command.__init__(self,entity)
        self.targetEnt = targetEnt

        #self.entity.desiredSpeed = self.entity.maxSpeed

    def tick(self, dt):
        v1 = self.entity.pos
        v2 = self.targetEnt.pos
        
        diff = v2 - v1
        
        self.entity.quaternion = v1.getRotationTo(diff, ogre.Vector3(0,0,1))
        self.entity.quaternion.normalise()

