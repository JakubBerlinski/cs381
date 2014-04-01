# Graphics manager. Manage graphics. 

import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS

class GfxMgr:
	def __init__(self, engine):
		self.engine = engine
		pass

	def init(self):
		self.createRoot()
		self.defineResources()
		self.setupRenderSystem()
		self.createRenderWindow()
		self.initializeResourceGroups()
		self.setupScene()
		self.createGroundPlane()

	def tick(self, dt):
		self.root.renderOneFrame()

	def stop(self):
		pass

	def createRoot(self):
		self.root = ogre.Root()

	def defineResources(self):
		cf = ogre.ConfigFile()
		cf.load("resources.cfg")

		seci = cf.getSectionIterator()
		while seci.hasMoreElements():
			secName = seci.peekNextKey()
			settings = seci.getNext()

			for item in settings:
				typeName = item.key
				archName = item.value
				ogre.ResourceGroupManager.getSingleton().addResourceLocation(archName, typeName, secName)

	def setupRenderSystem(self):
		if not self.root.restoreConfig() and not self.root.showConfigDialog():
			raise Exception("User canceled the config dialog -> Application.setupRenderSystem()")

	def createRenderWindow(self):
		self.windowGfx = self.root.initialise(True, "Assignment 5 Render Window")

	def initializeResourceGroups(self):
		ogre.TextureManager.getSingleton().setDefaultNumMipmaps(5)
		ogre.ResourceGroupManager.getSingleton().initialiseAllResourceGroups()

	def setupScene(self):
		self.sceneManager = self.root.createSceneManager(ogre.ST_GENERIC, "Default SceneManager")
		self.camera = self.sceneManager.createCamera("Camera")

		camNode = self.sceneManager.getRootSceneNode().createChildSceneNode('CamNode1', (-400, 200, 400))
		camNode.yaw(ogre.Degree(-45))
		node = camNode.createChildSceneNode('PitchNode1')
		node.attachObject(self.camera)

		self.viewPort = self.root.getAutoCreatedWindow().addViewport(self.camera)

	def createGroundPlane(self):
		self.sceneManager.ambientLight = 1, 1, 1
		plane = ogre.Plane((0,1,0), 0)
		meshManager = ogre.MeshManager.getSingleton()
		meshManager.createPlane('Ground', 'General', plane, 10000, 10000, 20, 20, True, 1, 5, 5, (0,0,1))
		ent = self.sceneManager.createEntity('GroundEntity', 'Ground')
		self.sceneManager.getRootSceneNode().createChildSceneNode().attachObject(ent)
		ent.setMaterialName('OceanCg')
		ent.castShadows = False
		self.sceneManager.setSkyDome(True, 'Examples/CloudySky', 5, 8)
            
	def createGent(self, mid, mesh, pos, yaw):
		e = self.sceneManager.createEntity(mid, mesh)
		node = self.sceneManager.getRootSceneNode().createChildSceneNode(mid + 'node', pos)
		node.attachObject(e)
		return node
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
