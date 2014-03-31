class SelectionMgr:
    def __init__(self, engine):
		self.engine = engine
		self.selectedEntIndex = 0
        self.selectedEnt = []
		print "Starting Selection Manager"

    def init(self):
		pass

    def tick(self, dt):
		pass
		
	def selectNextEnt(self):
		if self.selectedEntIndex >= self.engine.entityMgr.nEnts - 1:
			self.selectedEntIndex = 0
		else:
			self.selectedEntIndex += 1
		selectedEnt[:] = []
		self.selectedEnt.append(self.engine.entityMgr.ents[self.selectedEntIndex])
		
	def deselectEnt(self):
		pass
