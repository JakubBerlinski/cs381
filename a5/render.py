# Simple ORIENTED Physics for 38Engine
# vel is rate of change of pos
# Sushil Louis

import utils
import math

class Renderable:
	def __init__(self, ent, sceneManager, uid):
		self.ent = ent
		self.uid = uid
		self.sceneManager = sceneManager
		self.createNode()

	def tick(self, dtime):
		#----------position-----------------------------------
		self.ent.node.setPosition(self.ent.pos)
		#------------heading----------------------------------
		self.ent.node.resetOrientation()
		self.ent.node.yaw(self.ent.heading)

	def createNode(self):
		print self.ent.id
		e = self.sceneManager.createEntity(str(self.uid), self.ent.mesh)
		node = self.sceneManager.getRootSceneNode().createChildSceneNode(str(self.uid), self.ent.pos)
		node.attachObject(e)
		self.ent.node = node