import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import SampleFramework as sf

class Entity:
    def __init__(self, name, mesh = "", pos = ogre.Vector3(0,0,0), vel = ogre.Vector3(0,0,0), yaw = 0):
        self.name = name
        self.pos = pos
        self.vel = vel
        self.mesh = mesh
        self.yaw = yaw
        self.physics = Physics(self)

    def tick(self, time):
        self.physics.tick(time)

class Physics:
    def __init__(self, entity):
        self.entity = entity

    def tick(self, time):
        pos = self.entity.pos + self.entity.vel * time
        self.entity.pos = pos

class ObjectFrameListener(sf.FrameListener):
    def __init__(self, renderWindow, camera, sceneManager, entities, ogreEntities):
        sf.FrameListener.__init__(self, renderWindow, camera)

        self.toggle = 0
        self.mouseDown = False

        self.camNode = camera.parentSceneNode.parentSceneNode
        self.sceneManager = sceneManager

        self.rotate = 0.13
        self.move = 250

        self.entities = entities
        self.ogreEntities = ogreEntities
        self.oldTime = 0
        self.newTime = 0
        self.nodeNum = 0
        self.moveScale = 0.0

    def frameStarted(self, frameEvent):
        self.newTime = frameEvent.timeSinceLastFrame
        dt = self.newTime - self.oldTime * 10
        for i in self.entities:
            node = self.sceneManager.getSceneNode(i.name)
            i.tick(dt)
            node.setPosition(i.pos)

        self.oldTime = frameEvent.timeSinceLastFrame

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
        # Move Forward.
        if self.Keyboard.isKeyDown(OIS.KC_A):
            self.translateVector.x = -self.moveScale

        if self.Keyboard.isKeyDown(OIS.KC_D):
            self.translateVector.x = self.moveScale

        if self.Keyboard.isKeyDown(OIS.KC_W):
            self.translateVector.z = -self.moveScale

        if self.Keyboard.isKeyDown(OIS.KC_S):
            self.translateVector.z = self.moveScale
        # Move Up.        
        if self.Keyboard.isKeyDown(OIS.KC_R):
            transVector.y += self.move / 20
        # Move Down.
        if self.Keyboard.isKeyDown(OIS.KC_F):
            transVector.y -= self.move / 20

        # Move the cube using keyboard input.
        if self.Keyboard.isKeyDown(OIS.KC_TAB) and self.toggle < 0:
            self.toggle = 0.5
            self.ogreEntities[self.nodeNum].setMaterialName('whitebox')
            self.nodeNum += 1
            if self.nodeNum == self.entities.__len__():
                self.nodeNum = 0
            self.ogreEntities[self.nodeNum].setMaterialName('Examples/Rockwall')

        if self.Keyboard.isKeyDown(OIS.KC_DOWN):
            self.entities[self.nodeNum].vel += ogre.Vector3(0.5,0,0)

        if self.Keyboard.isKeyDown(OIS.KC_UP):
            self.entities[self.nodeNum].vel += ogre.Vector3(-0.5,0,0)

        if self.Keyboard.isKeyDown(OIS.KC_LEFT):
            self.entities[self.nodeNum].vel += ogre.Vector3(0,0,0.5)

        if self.Keyboard.isKeyDown(OIS.KC_RIGHT):
            self.entities[self.nodeNum].vel += ogre.Vector3(0,0,-0.5)

        if self.Keyboard.isKeyDown(OIS.KC_PGDOWN):
            self.entities[self.nodeNum].vel += ogre.Vector3(0,0.5,0)

        if self.Keyboard.isKeyDown(OIS.KC_PGUP):
            self.entities[self.nodeNum].vel += ogre.Vector3(0,-0.5,0)

        if self.Keyboard.isKeyDown(OIS.KC_SPACE):
            self.entities[self.nodeNum].vel = ogre.Vector3(0,0,0)
 
        # Translate the camera based on time.
        #self.camNode.translate(self.camNode.orientation * transVector * frameEvent.timeSinceLastFrame)
        self.camera.moveRelative(transVector)
 
        # If the escape key is pressed end the program.
        return not self.Keyboard.isKeyDown(OIS.KC_ESCAPE)


class MovingApplication(sf.Application):
    def _createScene(self):
        sceneManager = self.sceneManager
        sceneManager.ambientLight = (1, 1, 1)
        surfaceHeight = 0
        self.entities = []
        self.ogreEntities = []
        self.entities.append(Entity("cube1", mesh="cube.mesh", vel=ogre.Vector3(0,0,0), pos=ogre.Vector3(0,100,0)))
        self.entities.append(Entity("cube2", mesh="cube.mesh", vel=ogre.Vector3(0,0,0), pos=ogre.Vector3(0,200,0)))

        # Setup a mesh entity and attach it to a scene node.
        for i in self.entities:
            entity = sceneManager.createEntity(i.name, i.mesh)
            self.ogreEntities.append(entity);
            node = sceneManager.getRootSceneNode().createChildSceneNode(i.name)
            node.attachObject(entity)

        self.ogreEntities[0].setMaterialName ('Examples/Rockwall')

        # Setup a ground plane.
        plane = ogre.Plane ((0, 1, 0), 0)
        meshManager = ogre.MeshManager.getSingleton ()
        meshManager.createPlane ('Ground', 'General', plane, 10000, 10000, 20, 20, True, 1, 5, 5, (0, 0, 1))

        groundPlane = sceneManager.createEntity('GroundEntity', 'Ground')
        groundNode = sceneManager.getRootSceneNode().createChildSceneNode('GroundPlane')
        groundNode.attachObject(groundPlane)
        groundNode.setPosition(0,surfaceHeight,0)
        groundPlane.setMaterialName ('Examples/Rockwall')

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
        self.frameListener = ObjectFrameListener(self.renderWindow, self.camera, self.sceneManager, self.entities, self.ogreEntities)
        self.root.addFrameListener(self.frameListener)
        self.frameListener.showDebugOverlay(True)

if __name__ == '__main__':
    ta = MovingApplication()
    ta.go()
