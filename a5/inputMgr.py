import ogre.io.OIS as OIS
import ogre.renderer.OGRE as ogre

class InputMgr:
	def __init__(self, engine):
		self.engine = engine
		self.sceneManager = self.engine.gfxMgr.sceneManager
		self.camNode = self.engine.gfxMgr.camera.parentSceneNode.parentSceneNode
		self.rotate = 0.50
		self.move = 400
		
	def init(self):
		self.setupInputSystem()

	def tick(self, dt):
		self.manageInput(dt)

	def setupInputSystem(self):
		windowHandle = 0
		self.renderWindow = self.engine.gfxMgr.root.getAutoCreatedWindow()
		windowHandle = self.renderWindow.getCustomAttributeUnsignedLong("WINDOW")
		paramList = [("WINDOW", str(windowHandle))]
		t = [("x11_mouse_grab", "false"), ("x11_mouse_hide", "false")]
		paramList.extend(t)
		self.inputManager = OIS.createPythonInputSystem(paramList)

		try:
			self.keyboard = self.inputManager.createInputObjectKeyboard(OIS.OISKeyboard, False)
			self.mouse = self.inputManager.createInputObjectMouse(OIS.OISMouse, False)
		except Exception, e:
			raise e
			
	def manageInput(self, dt):
		self.keyboard.capture()
		self.mouse.capture()
		print self.mouse.getPosition()
		transVector = ogre.Vector3(0,0,0)
		
		if self.keyboard.isKeyDown(OIS.KC_W):
			transVector.z -= self.move
		if self.keyboard.isKeyDown(OIS.KC_S):
			transVector.z += self.move
		if self.keyboard.isKeyDown(OIS.KC_A):
			transVector.x -= self.move
		if self.keyboard.isKeyDown(OIS.KC_D):
			transVector.x += self.move
		if self.keyboard.isKeyDown(OIS.KC_PGUP):
			transVector.y += self.move
		if self.keyboard.isKeyDown(OIS.KC_PGDOWN):
			transVector.y -= self.move
		if self.keyboard.isKeyDown(OIS.KC_Q):
			self.camNode.yaw(ogre.Degree(self.rotate))
		if self.keyboard.isKeyDown(OIS.KC_E):
			self.camNode.yaw(ogre.Degree(-self.rotate))
		if self.keyboard.isKeyDown(OIS.KC_Z):
			self.camNode.pitch(ogre.Degree(self.rotate))
		if self.keyboard.isKeyDown(OIS.KC_X):
			self.camNode.pitch(ogre.Degree(-self.rotate))
		if self.keyboard.isKeyDown(OIS.KC_ESCAPE):
			self.engine.keepRunning = False

		self.camNode.translate(self.camNode.orientation * transVector * dt)
