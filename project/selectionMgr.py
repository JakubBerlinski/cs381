
class SelectionMgr(object):
    def __init__(self, engine):
        self.engine = engine
        
    def init(self):
        self.entMgr = self.engine.entityMgr
        self.currentEntityIndex = -1
        self.selectedEntities = []

    def stop(self):
        pass

    def deselectAllEntities(self):
        for i, ent in self.entMgr.ents.iteritems():
            ent.node.showBoundingBox(False)

        self.selectedEntities = []

    def selectNextEntity(self, append = False):
        if self.entMgr.nEnts != 0:
            if not append:
                self.deselectAllEntities()

            self.currentEntityIndex = (self.currentEntityIndex + 1) % self.entMgr.nEnts
            currentEntity = self.entMgr.ents[self.currentEntityIndex]
            if not currentEntity in self.selectedEntities:
                self.selectedEntities.append(currentEntity)
                currentEntity.node.showBoundingBox(True)
                print 'Selected Entity:', currentEntity.uiname

            return currentEntity

    def selectEntityOnClick(self, entID, append = False):
        if self.entMgr.nEnts != 0:
            if not append:
                self.deselectAllEntities()

            self.currentEntityIndex = int(entID)
            currentEntity = self.entMgr.ents[self.currentEntityIndex]
            if not currentEntity in self.selectedEntities:
                self.selectedEntities.append(currentEntity)
                currentEntity.node.showBoundingBox(True)
                print 'Selected Entity:', currentEntity.uiname

            return currentEntity

        
    def tick(self, dt):
        pass
