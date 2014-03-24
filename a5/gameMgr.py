import ogre.renderer.OGRE as ogre

class GameMgr:
    def __init__(self, engine):
        self.engine = engine
        print "starting Game mgr"
        pass

    def init(self):
        self.loadLevel()


    def loadLevel(self):
        self.game1()
        

    def game1(self):
        x = 0
        i = 0
        for entType in self.engine.entityMgr.entTypes:
            print "GameMgr Creating", str(entType)
            ent = self.engine.entityMgr.createEnt(entType, pos = ogre.Vector3(x, 0, 0))
            gfxNode = self.engine.gfxMgr.createGent(ent.uiname + str(i), ent.mesh, ent.pos, ent.heading)
            ent.node = gfxNode
            print "GameMgr Created: ", ent.uiname, ent.id, ent.node
            x += 300
            i += 1

    def tick(self, dt):
        pass

    def stop(self):
        pass
        

