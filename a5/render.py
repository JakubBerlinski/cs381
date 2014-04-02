from math import radians
import ogre.renderer.OGRE as ogre

class Renderable:
	def __init__(self, ent, sceneManager, uid):
		self.ent = ent
		self.uid = uid
		self.sceneManager = sceneManager
		self.createNode()

	def tick(self, dtime):
		self.ent.node.setPosition(self.ent.pos)
		self.ent.node.setOrientation(ogre.Quaternion(radians(-self.ent.heading), ogre.Vector3(0,1,0)))

	def createNode(self):
		print self.ent.id
		e = self.sceneManager.createEntity(str(self.uid), self.ent.mesh)
		node = self.sceneManager.getRootSceneNode().createChildSceneNode(str(self.uid), self.ent.pos)
		node.attachObject(e)
		self.ent.node = node
