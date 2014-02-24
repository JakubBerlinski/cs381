import ogre.renderer.OGRE as ogre
import SampleFramework as sf
 
class TutorialApplication(sf.Application):
 
   def _createScene(self):
		sceneManager = self.sceneManager
		sceneManager.ambientLight = (1, 1, 1)
		sceneManager.shadowTechnique = ogre.SHADOWTYPE_STENCIL_ADDITIVE
 
        # Setup a mesh object.
		ent = sceneManager.createEntity('Ninja', 'ninja.mesh')
		ent.castShadows = True
		sceneManager.getRootSceneNode().createChildSceneNode().attachObject(ent)
 
        # Setup a ground plane.
		plane = ogre.Plane ((0, 1, 0), 0)
		meshManager = ogre.MeshManager.getSingleton ()
		meshManager.createPlane ('Ground', 'General', plane,
                                     10000, 10000, 20, 20, True, 1, 5, 5, (0, 0, 1))
		ent = sceneManager.createEntity('GroundEntity', 'Ground')
		sceneManager.getRootSceneNode().createChildSceneNode ().attachObject (ent)
		ent.setMaterialName ('Examples/Rockwall')
		ent.castShadows = False
  

 
   def _createCamera (self):
		self.camera =  self.sceneManager.createCamera ('PlayerCam')
		self.camera.position = (0, 150, -500)
		self.camera.lookAt ((0, 0, 0))
		self.camera.nearClipDistance = 5
 
   def _createViewports (self):
		viewport = self.renderWindow.addViewport (self.camera)
		viewport.backGroundColor = (0, 0, 0)
		self.camera.aspectRatio = float (viewport.actualWidth) / float (viewport.actualHeight)
 
if __name__ == '__main__':
   ta = TutorialApplication()
   ta.go()
