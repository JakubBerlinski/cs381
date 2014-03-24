class SelectionMgr:
    def __init__(self, engine):
		self.engine = engine
		print "Starting Selection Manager"

    def init(self):
		self.selectedEntities = {}

    def tick(self, dt):
		pass
