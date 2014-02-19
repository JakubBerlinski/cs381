class Physics:
    def __init__(self, entity):
        self.entity = entity

    def tick(self, time):
    	pos = self.entity.pos + self.entity.vel * time
    	self.entity.pos = pos