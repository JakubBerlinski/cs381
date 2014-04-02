import ogre.io.OIS as OIS
import ogre.renderer.OGRE as ogre
import sys

class InputMgr:
	def __init__(self, engine):
		self.engine = engine
		self.sceneManager = self.engine.gfxMgr.sceneManager
		self.camNode = self.engine.gfxMgr.camera.parentSceneNode#.parentSceneNode
		self.rotate = 0.50
		self.move = 400
		self.camera = self.engine.gfxMgr.camera
		self.raySceneQuery = self.sceneManager.createRayQuery(ogre.Ray())
		self.toggle = 0
		
	def init(self):
		self.setupInputSystem()

	def tick(self, dt):
		self.manageInput(dt)

	def setupInputSystem(self):
		windowHandle = 0
		self.renderWindow = self.engine.gfxMgr.root.getAutoCreatedWindow()
		windowHandle = self.renderWindow.getCustomAttributeUnsignedLong("WINDOW")
		paramList = [("WINDOW", str(windowHandle))]
		if sys.platform == 'win32':
			t = [('w32_mouse', 'DISCL_FOREGROUND'), ('w32_mouse', 'DISCL_NONEXCLUSIVE')]
		else:
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

		if self.toggle >= 0:
			self.toggle -= dt

		mouseState = self.mouse.getMouseState()
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

		if self.toggle < 0 and mouseState.buttonDown(OIS.MB_Left):
			mouseState.width = self.engine.gfxMgr.windowGfx.getWidth()
			mouseState.height = self.engine.gfxMgr.windowGfx.getHeight()
			print mouseState.X.abs, mouseState.Y.abs
			mouseRay = self.camera.getCameraToViewportRay(mouseState.X.abs / float(mouseState.width), mouseState.Y.abs / float(mouseState.height))
			self.raySceneQuery.setRay(mouseRay)
			self.raySceneQuery.setSortByDistance(True)
			result = self.raySceneQuery.execute()
			if len(result) > 0:
				print len(result)
				for item in result:
					ent = item.movable
					if ent.getName() != "Camera" and ent.getName() != "GroundEntity": 
						print ent.getName()
						self.engine.selectionMgr.selectClickedEnt(ent.getName())
						ent.getParentSceneNode().showBoundingBox(True)

		self.camNode.translate(self.camNode.orientation * transVector * dt)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
