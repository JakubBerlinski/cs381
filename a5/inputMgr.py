import ogre.io.OIS as OIS
import ogre.renderer.OGRE as ogre

class CameraListener(ogre.FrameListener):
	def __init__(self, keyboard, camera, sceneManager, engine):
		ogre.FrameListener.__init__(self)
		self.keyboard = keyboard
		self.camNode = camera.parentSceneNode.parentSceneNode
		self.sceneManager = sceneManager
		self.engine = engine
		self.rotate = 0.50
		self.move = 400

	def frameStarted(self, evt):
		self.keyboard.capture()

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
		if self.keyboard.isKeyDown(OIS.KC_ESCAPE):
			self.engine.keepRunning = False

		self.camNode.translate(self.camNode.orientation * transVector * evt.timeSinceLastFrame)
		return True

	def frameEnded(self, evt):
		pass
		return True

	def frameRenderingQueued(self, evt):
		pass
		return True

class InputMgr:
	def __init__(self, engine):
		self.engine = engine

	def init(self):
		self.setupInputSystem()
		self.createFrameListener()

	def tick(self, dt):
		pass

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

	def createFrameListener(self):
		self.cameraListener = CameraListener(self.keyboard, self.engine.gfxMgr.camera, self.engine.gfxMgr.sceneManager, self.engine)
		self.engine.gfxMgr.root.addFrameListener(self.cameraListener)
