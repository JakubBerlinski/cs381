import ogre.io.OIS as OIS
import ogre.renderer.OGRE as ogre
import utils

class ControlMgr:
	def __init__(self, engine):
		self.engine = engine
		self.sceneManager = self.engine.gfxMgr.sceneManager
		self.toggle = 0
		self.keyboard = self.engine.inputMgr.keyboard

	def init(self):
		pass

	def tick(self, dt):
		 self.manageInput(dt)
		 for uid, ent in self.engine.entityMgr.ents.iteritems():
		  	ent.tick(dt)
			
	def manageInput(self, dt):
		self.keyboard.capture()
		if self.toggle >= 0:
			self.toggle -= dt
			
		selectedEnt = self.engine.entityMgr.selectedEnt
		if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_UP):
			self.toggle = 0.25
			selectedEnt.desiredSpeed = utils.clamp(selectedEnt.desiredSpeed + selectedEnt.deltaSpeed, 0, selectedEnt.maxSpeed)
			print "Speeding Up", selectedEnt.desiredSpeed
			
		if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_DOWN):
			self.toggle = 0.25
			selectedEnt.desiredSpeed = utils.clamp(selectedEnt.desiredSpeed - selectedEnt.deltaSpeed, 0, selectedEnt.maxSpeed)
			print "Slowing Down", selectedEnt.desiredSpeed
			
		if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_LEFT):
			self.toggle = 0.25
			selectedEnt.desiredHeading += selectedEnt.deltaYaw
			selectedEnt.desiredHeading = utils.fixAngle(selectedEnt.desiredHeading)
			print "Turn left", selectedEnt.desiredHeading
			
		if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_RIGHT):
			self.toggle = 0.25
			selectedEnt.desiredHeading -= selectedEnt.deltaYaw
			selectedEnt.desiredHeading = utils.fixAngle(selectedEnt.desiredHeading)
			print "Turn right", selectedEnt.desiredHeading
			
		if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_TAB):
			self.toggle = 0.25
			selectedEnt.node.showBoundingBox(False)
			selectedEnt = self.engine.entityMgr.selectNextEnt()
			print "Selected: ", str(selectedEnt)
			selectedEnt.node.showBoundingBox(True)

