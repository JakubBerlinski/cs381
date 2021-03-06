import ogre.io.OIS as OIS
import ogre.renderer.OGRE as ogre

class ControlMgr:
	def __init__(self, engine):
		self.engine = engine
		self.sceneManager = self.engine.gfxMgr.sceneManager
		self.toggle = 0
		self.keyboard = self.engine.inputMgr.keyboard
		self.mouse = self.engine.inputMgr.mouse
		self.camera = self.engine.gfxMgr.camera
		self.raySceneQuery = self.sceneManager.createRayQuery(ogre.Ray())

	def init(self):
		pass

	def tick(self, dt):
		 self.manageInput(dt)
		 for uid, ent in self.engine.entityMgr.ents.iteritems():
		  	ent.tick(dt)
			
	def manageInput(self, dt):
		self.keyboard.capture()
		self.mouse.capture()
		mouseState = self.mouse.getMouseState()
		if self.toggle >= 0:
			self.toggle -= dt

		selectedEnt = self.engine.selectionMgr.selectedEnt
		
		if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_UP):
			self.toggle = 0.25
			for ent in selectedEnt:
				ent.desiredSpeed += 1
			
		if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_DOWN):
			self.toggle = 0.25
			for ent in selectedEnt:
				ent.desiredSpeed -= 1
			
		if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_LEFT):
			self.toggle = 0.25
			for ent in selectedEnt:
				ent.desiredHeading -= 1
			
		if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_RIGHT):
			self.toggle = 0.25
			for ent in selectedEnt:
				ent.desiredHeading += 1
			
		if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_TAB) and not self.keyboard.isKeyDown(OIS.KC_LSHIFT):
			self.toggle = 0.25
			for ent in selectedEnt:
				ent.node.showBoundingBox(False)
			selectedEnt = self.engine.selectionMgr.selectNextEnt()

			print selectedEnt[0].mesh
			selectedEnt[0].node.showBoundingBox(True)
			
		if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_TAB) and self.keyboard.isKeyDown(OIS.KC_LSHIFT):
			self.toggle = 0.25
			selectedEnt = self.engine.selectionMgr.appendEnt()
			for ent in selectedEnt:
				ent.node.showBoundingBox(True)
				
		if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_SPACE):
			self.toggle = 0.25
			for ent in selectedEnt:
				ent.vel = ogre.Vector3(0,0,0)
				ent.speed = 0
				ent.desiredSpeed = 0
