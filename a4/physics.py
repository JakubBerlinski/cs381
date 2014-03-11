class Physics:
	def __init__(self, entity):
		self.entity = entity

	def tick(self, time):
		self.entity.pos = self.entity.pos + self.entity.vel * time