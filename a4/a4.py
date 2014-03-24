import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import SampleFramework as sf

from entitymgr import EntityMgr

class EntityFrameListener(ogre.FrameListener):
    def __init__(self, entityMgr):
        ogre.FrameListener.__init__(self)
        self.entityMgr = entityMgr

    def frameStarted(self, frameEvent):
        self.entityMgr.updateEntities(frameEvent.timeSinceLastFrame)
        return True

class InputFrameListener(sf.FrameListener):
    def __init__(self, renderWindow, camera, sceneManager, entityMgr):
        sf.FrameListener.__init__(self, renderWindow, camera)
        self.toggle = 0
        self.mouseDown = False
        self.camNode = camera.parentSceneNode.parentSceneNode
        self.sceneManager = sceneManager
        self.rotate = 0.13
        self.move = 500
        self.entityMgr = entityMgr
        self.nodeNum = 0
        self.moveScale = 0.0

    def frameStarted(self, frameEvent):
        if(self.renderWindow.isClosed()):
            return False
 
        # Capture and update each input device.
        self.Keyboard.capture()
        self.Mouse.capture()
 
        # Get the current mouse state.
        currMouse = self.Mouse.getMouseState()

        self.moveScale = self.move * frameEvent.timeSinceLastFrame
  
        # Update the mouseDown boolean.            
        self.mouseDown = currMouse.buttonDown(OIS.MB_Left)
 
        # Update the toggle timer.
        if self.toggle >= 0:
            self.toggle -= frameEvent.timeSinceLastFrame

        return True
  
    def _processUnbufferedKeyInput(self, frameEvent):
        # Move the camera using keyboard input.
        transVector = ogre.Vector3(0, 0, 0)
        
        if self.Keyboard.isKeyDown(OIS.KC_A):
            self.translateVector.x = -self.moveScale

        if self.Keyboard.isKeyDown(OIS.KC_D):
            self.translateVector.x = self.moveScale

        if self.Keyboard.isKeyDown(OIS.KC_W):
            self.translateVector.z = -self.moveScale

        if self.Keyboard.isKeyDown(OIS.KC_S):
            self.translateVector.z = self.moveScale   

        if self.Keyboard.isKeyDown(OIS.KC_R):
            transVector.y += self.move / 20

        if self.Keyboard.isKeyDown(OIS.KC_F):
            transVector.y -= self.move / 20

        # Move the cube using keyboard input.
        if self.Keyboard.isKeyDown(OIS.KC_TAB) and self.toggle < 0:
			self.toggle = 0.3
			self.entityMgr.updateSelection()

        if self.Keyboard.isKeyDown(OIS.KC_DOWN):
            self.entityMgr.updateSelectedEntity(0)

        if self.Keyboard.isKeyDown(OIS.KC_UP):
            self.entityMgr.updateSelectedEntity(1)

        if self.Keyboard.isKeyDown(OIS.KC_LEFT):
            self.entityMgr.updateSelectedEntity(2)

        if self.Keyboard.isKeyDown(OIS.KC_RIGHT):
            self.entityMgr.updateSelectedEntity(3)

        if self.Keyboard.isKeyDown(OIS.KC_SPACE):
            self.entityMgr.updateSelectedEntity(4)
 
        # Translate the camera based on time.
        #self.camNode.translate(self.camNode.orientation * transVector * frameEvent.timeSinceLastFrame)
        # self.camera.moveRelative(transVector)
        self._moveCamera()
 
        # If the escape key is pressed end the program.
        return not self.Keyboard.isKeyDown(OIS.KC_ESCAPE)


class MovingApplication(sf.Application):
    def _createScene(self):
        sceneManager = self.sceneManager
        sceneManager.ambientLight = (1, 1, 1)
        self.surfaceHeight = 0
        self.entityMgr = EntityMgr(sceneManager)

        self.entityMgr.createEntity(sceneManager, "sailboat", mesh="sailboat.mesh", vel=ogre.Vector3(0,0,0), pos=ogre.Vector3(0,3,0))
        self.entityMgr.createEntity(sceneManager, "destroyer", mesh="sleek.mesh", vel=ogre.Vector3(0,0,0), pos=ogre.Vector3(0,3,100))
        self.entityMgr.createEntity(sceneManager, "speedboat", mesh="5086_Boat.mesh", vel=ogre.Vector3(0,0,0), pos=ogre.Vector3(0,3,200))
        self.entityMgr.createEntity(sceneManager, "scout", mesh="cigarette.mesh", vel=ogre.Vector3(0,0,0), pos=ogre.Vector3(0,3,300))
        self.entityMgr.createEntity(sceneManager, "superspeedboat", mesh="boat.mesh", vel=ogre.Vector3(0,0,0), pos=ogre.Vector3(0,3,400))
        self.entityMgr.createEntity(sceneManager, "alienship", mesh="alienship.mesh", vel=ogre.Vector3(0,0,0), pos=ogre.Vector3(0,3,500))
        self.entityMgr.createEntity(sceneManager, "aircraftcarrier", mesh="cvn68.mesh", vel=ogre.Vector3(0,0,0), pos=ogre.Vector3(0,3,600))
        self.entityMgr.createEntity(sceneManager, "gunship", mesh="sleek.mesh", vel=ogre.Vector3(0,0,0), pos=ogre.Vector3(0,3,700))

        # self.ogreEntities[0].setMaterialName ('Examples/Rockwall')

        # Setup a ground plane.
        plane = ogre.Plane ((0, 1, 0), 0)
        meshManager = ogre.MeshManager.getSingleton ()
        meshManager.createPlane ('Ground', 'General', plane, 10000, 10000, 20, 20, True, 1, 5, 5, (0, 0, 1))

        groundPlane = sceneManager.createEntity('GroundEntity', 'Ground')
        groundNode = sceneManager.getRootSceneNode().createChildSceneNode('GroundPlane')
        groundNode.attachObject(groundPlane)
        groundNode.setPosition(0,self.surfaceHeight,0)
        groundPlane.setMaterialName ('Ocean2_Cg')

        # Setup the first camera node and pitch node and aim it.
        node = sceneManager.getRootSceneNode().createChildSceneNode('CamNode1', (-400, 200, 400))
        node.yaw(ogre.Degree(-45))
        node = node.createChildSceneNode('PitchNode1')
        node.attachObject(self.camera)

    def _createCamera(self):
        self.camera = self.sceneManager.createCamera('PlayerCam')
        self.camera.nearClipDistance = 5

    def _createViewports(self):
        viewport = self.renderWindow.addViewport (self.camera)
        viewport.backGroundColor = (0, 0, 0)
        self.camera.aspectRatio = float (viewport.actualWidth) / float (viewport.actualHeight)

    def _createFrameListener(self):
        self.inputframeListener = InputFrameListener(self.renderWindow, self.camera, self.sceneManager, self.entityMgr)
        self.root.addFrameListener(self.inputframeListener)

        self.entityFrameListener = EntityFrameListener(self.entityMgr)
        self.root.addFrameListener(self.entityFrameListener)

        # self.frameListener.showDebugOverlay(True)

if __name__ == '__main__':
    try:
        ta = MovingApplication()
        ta.go()
    except ogre.OgreException, e:
        print e
