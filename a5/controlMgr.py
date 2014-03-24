import ogre.io.OIS as OIS
import ogre.renderer.OGRE as ogre
import utils

class ControlListener(ogre.FrameListener):
	def __init__(self, keyboard, sceneManager, engine):
		ogre.FrameListener.__init__(self)
		self.keyboard = keyboard
		self.sceneManager = sceneManager
		self.engine = engine
		self.toggle = 0

	def frameStarted(self, evt):
		self.keyboard.capture()
	
		if self.toggle >= 0:
			self.toggle -= evt.timeSinceLastFrame

		selectedEnt = self.engine.entityMgr.selectedEnt
		if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_UP):
			self.toggle = 0.1
			selectedEnt.desiredSpeed = utils.clamp(selectedEnt.desiredSpeed + selectedEnt.deltaSpeed, 0, selectedEnt.maxSpeed)
			print "Speeding UP", selectedEnt.desiredSpeed

		if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_TAB):
			self.toggle = 0.1
			ent = self.engine.entityMgr.selectedEnt
			ent.node.showBoundingBox(False)
			self.engine.entityMgr.selectNextEnt()
			print "FrameListener: Selected: ", str(ent)
			ent.node.showBoundingBox(True)

		return True

	def frameEnded(self, evt):
		pass
		return True

	def frameRenderingQueued(self, evt):
		pass
		return True

class ControlMgr:
	def __init__(self, engine):
		self.engine = engine
		pass

	def init(self):
		self.createFrameListener()
		pass

	def tick(self, dt):
		for uid, ent in self.engine.entityMgr.ents.iteritems():
			ent.tick(dt)

	def createFrameListener(self):
		self.controlListener = ControlListener(self.engine.inputMgr.keyboard, self.engine.gfxMgr.sceneManager, self.engine)
		self.engine.gfxMgr.root.addFrameListener(self.controlListener)
