import ent
from ogre.renderer.OGRE import Vector3

class EntityMgr:
    def __init__(self, engine):
        print "starting ent mgr"
        self.engine = engine
        self.ents = {}
        self.nEnts = 0
        self.entTypes = [ent.DRONE, ent.WALL]
        self.deleteEnt = []
        
    def init(self):
        pass

    def createEnt(self, entType, pos = Vector3(0,0,0), yaw = 0, orientation = Vector3().ZERO):
        ent = entType(self.engine, self.nEnts, pos = pos, yaw = yaw, orientation = orientation)
        self.engine.gfxMgr.createOgreEntity(ent)
        ent.initAspects()

        self.ents[self.nEnts] = ent
        self.nEnts += 1

        return ent
        
    def destroyEnt(self, ent):
        self.engine.gfxMgr.destroyOgreEntity(ent)
        del self.ents[ent.id]
        
        ent = None

    def tick(self, dt):
        for ent in self.ents:
            self.ents[ent].tick(dt)
            
        for ent in self.deleteEnt:
            self.destroyEnt(ent)
        
        self.deleteEnt = []
            
        
