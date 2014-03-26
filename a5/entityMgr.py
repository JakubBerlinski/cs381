
import ogre.renderer.OGRE as ogre
import ent

class EntMgr:
    def __init__(self, engine):
        self.engine = engine
        print "starting entity manager"
        
    def init(self):
        self.ents = {}
        self.nEnts = 0
        self.selectedEntIndex = 0
        self.selectedEnt = None
        self.entTypes = [ent.CIGARETTE, ent.CVN68, ent.DDG51, ent.BOAT, ent.BOAT2, ent.SLEEK, ent.MONTEREY, ent.JETSKI, ent.ALIENSHIP, ent.SAILBOAT]

    def tick(self, dt):
        for uid, ent in self.ents.iteritems():
            ent.tick(dt)

    def stop(self):
        pass


    def createEnt(self, entType, pos = ogre.Vector3(0,0,0), yaw = 0):
        ent = entType(self.nEnts, self.engine.gfxMgr.sceneManager, pos = pos, yaw = yaw)

        self.ents[self.nEnts] = ent;
        self.selectedEnt = ent
        self.selectedEntIndex = self.nEnts;

        self.nEnts = self.nEnts + 1
        return ent

    def selectNextEnt(self):
        if self.selectedEntIndex >= self.nEnts - 1:
            self.selectedEntIndex = 0
        else:
            self.selectedEntIndex += 1
        self.selectedEnt = self.ents[self.selectedEntIndex]
        print "EntMgr selected: ", str(self.selectedEnt)
        return self.selectedEnt

    def getSelected(self):
        return self.selectedEnt



        





