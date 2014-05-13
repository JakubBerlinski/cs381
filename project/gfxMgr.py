from ogre.renderer.OGRE import Vector3
import ogre.renderer.OGRE as ogre
from math import radians

class GfxMgr(object):
    def __init__(self, engine):
        self.engine = engine
        
    def init(self):
        self.root = ogre.Root()

        # define resources
        cf = ogre.ConfigFile()
        cf.load('resources.cfg')

        seci = cf.getSectionIterator()
        while seci.hasMoreElements():
            secName = seci.peekNextKey()
            settings = seci.getNext()

            for item in settings:
                typeName = item.key
                archName = item.value
                ogre.ResourceGroupManager.getSingleton().addResourceLocation(archName, typeName, secName)

        # setup render system
        if not self.root.restoreConfig() and not self.root.showConfigDialog():
            raise Exception('Config Dialog Closed...')

        # create render window
        self.renderWindow = self.root.initialise(True, 'CS381 -- Cameron Rowe and Jakub Berlinski')

        # initialize resource groups
        ogre.TextureManager.getSingleton().setDefaultNumMipmaps(5)
        ogre.ResourceGroupManager.getSingleton().initialiseAllResourceGroups()

        # setup scene
        self.sceneManager = self.root.createSceneManager(ogre.ST_GENERIC, 'Default SceneManager')
        self.sceneManager.shadowTechnique = ogre.SHADOWTYPE_STENCIL_ADDITIVE
        self.camera = self.sceneManager.createCamera('Camera')
        self.root.getAutoCreatedWindow().addViewport(self.camera)

        self.camera.setPosition(ogre.Vector3(0, 30, 0))
        self.camera.lookAt(ogre.Vector3(0, 0, -300))
        self.camera.nearClipDistance = 5

        sceneManager = self.sceneManager
        sceneManager.ambientLight = (0.1,0.1,0.1)

        light = sceneManager.createLight('PointLight')
        light.type = ogre.Light.LT_POINT
        light.position = (0, 150, 0)
        light.diffuseColour = (1,1,1)
        light.specularColour = (1,1,1)
 
        # Setup a ground plane.
        self.groundPlane = ogre.Plane ((0, 1, 0), 0)
        meshManager = ogre.MeshManager.getSingleton()

        meshManager.createPlane ('Ground', 'General', self.groundPlane,
                                     10000, 10000, 20, 20, True, 1, 5, 5, (0, 0, 1))
        ent = sceneManager.createEntity('GroundEntity', 'Ground')
        sceneManager.getRootSceneNode().createChildSceneNode().attachObject (ent)
        ent.setMaterialName ('Examples/Rockwall')
        ent.castShadows = False

        self.createLevelElement('wall1', 'wall.mesh', 'wall', Vector3(100,0,0), Vector3(0,0,0))
        self.createLevelElement('wall2', 'wall.mesh', 'wall', Vector3(-100,0,0), Vector3(0,0,0))
        self.createLevelElement('wall3', 'wall.mesh', 'wall', Vector3(0,0,100), Vector3(0,1,0))
        self.createLevelElement('wall4', 'wall.mesh', 'wall', Vector3(0,0,-100), Vector3(0,1,0))

        self.createLevelElement('piller1', 'piller.mesh', 'piller', Vector3(45,0,65), Vector3(0,0,0))
        self.createLevelElement('piller2', 'piller.mesh', 'piller', Vector3(-85,0,65), Vector3(0,0,0))
        self.createLevelElement('piller3', 'piller.mesh', 'piller', Vector3(-85,0,-65), Vector3(0,0,0))
        self.createLevelElement('piller4', 'piller.mesh', 'piller', Vector3(45,0,-65), Vector3(0,0,0))
        self.createLevelElement('piller5', 'piller.mesh', 'piller', Vector3(-20,0,0), Vector3(0,0,0))

        sceneManager.setSkyDome (True, "Examples/CloudySky", 5, 8)
        

    def stop(self):
        pass

    def createLevelElement(self, name, mesh, texture, position, rotation):
        ent = self.sceneManager.createEntity(name, mesh)
        ent.castShadows = True
        node = self.sceneManager.getRootSceneNode().createChildSceneNode(name + 'Node')
        node.attachObject(ent)
        node.setPosition(position)
        node.setOrientation(1,rotation.x, rotation.y, rotation.z)
        ent.setMaterialName(texture)

    def createOgreEntity(self, ent):
        sceneManager = self.sceneManager
        ogreEntity = sceneManager.createEntity(str(ent.id), ent.mesh)
        node = sceneManager.getRootSceneNode().createChildSceneNode(str(ent.id) + 'Node')
        node.attachObject(ogreEntity)
        node.setPosition(ent.pos)
        #node.setOrientation(1, ent.orientation.x, ent.orientation.y, ent.orientation.z)
        node.setOrientation(self.engine.inputMgr.camera.getDerivedOrientation())
        node.scale(ent.scale, ent.scale, ent.scale)
        ogreEntity.setMaterialName(ent.material)
        ent.node = node
        ogreEntity.castShadows = True
        
        
    def destroyOgreEntity(self, ent):
        self.sceneManager.destroyEntity(str(ent.id))
        self.sceneManager.getRootSceneNode().removeAndDestroyChild(str(ent.id) + 'Node')
        
    def tick(self, dt):
        self.root.renderOneFrame(dt)
        
    
