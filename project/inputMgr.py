
import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import sys, ai, ent
from util import is64Bit

class InputMgr(object):
    def __init__(self, engine):
        self.engine = engine
        self.camera = engine.gfxMgr.camera
        self.toggle = 0.0
        self.missileToggle = 0.0
        self.spawnBullet = False
        self.spawnMissile = False

    def init(self):
        renderWindow = self.engine.gfxMgr.renderWindow
        if is64Bit():
            windowHandle = renderWindow.getCustomAttributeUnsignedLong("WINDOW")
        else:
            windowHandle = renderWindow.getCustomAttributeInt("WINDOW")
        paramList = [('WINDOW', str(windowHandle))]

        '''
        if sys.platform == 'win32':
            paramList.extend([('w32_mouse', 'DISCL_FOREGROUND'), ('w32_mouse', 'DISCL_NONEXCLUSIVE')])
        else:
            paramList.extend([('x11_mouse_grab', 'false'), ('x11_mouse_hide', 'false')])

        '''
        self.oisMgr = OIS.createPythonInputSystem(paramList)
        try:
            self.keyboard = self.oisMgr.createInputObjectKeyboard(OIS.OISKeyboard, True)
            self.mouse = self.oisMgr.createInputObjectMouse(OIS.OISMouse, True)
            try:
                self.joystick = self.oisMgr.createInputObjectJoyStick(OIS.OISJoyStick, True)
            except:
                self.joystick = False

        except Exception, e:
            print "ERROR: Unable to initialize mouse, keyboard, or joystick"
            raise e

        self.moveSpeed = 100
        self.moveScale = 0.0
        self.rotationScale = 0.0
        self.translateVector = ogre.Vector3(0.0,0.0,0.0)
        self.soundPlaying = False
        self.moveUp = self.moveDown = False
        self.joystickSensitivity = 1.0

        self.rotationX = ogre.Degree(0.0)
        self.rotationY = ogre.Degree(0.0)
        self.rotateSpeed =  ogre.Degree(36)

        ms = self.mouse.getMouseState()
        ms.width = renderWindow.getWidth()
        ms.height = renderWindow.getHeight()
        self.raySceneQuery = self.engine.gfxMgr.sceneManager.createRayQuery(ogre.Ray())

    def stop(self):
        self.oisMgr.destroyInputObjectKeyboard(self.keyboard)
        self.oisMgr.destroyInputObjectMouse(self.mouse)

        if self.joystick:
            self.oisMgr.destroyInputObjectJoyStick(self.joystick)

        OIS.InputManager.destroyInputSystem(self.oisMgr)
        self.oisMgr = None

    def tick(self, dt):
        self.keyboard.capture()
        self.mouse.capture()

        self.spawnBullet = False
        self.spawnMissile = False
        if self.joystick:
            self.joystick.capture()

        if self.toggle >= 0.0:
            self.toggle -= dt
            
        if self.missileToggle >= 0.0:
            self.missileToggle -= dt
            
        ## Move about 100 units per second
        self.moveScale = self.moveSpeed * dt
        ## Take about 10 seconds for full rotation
        self.rotScale = self.rotateSpeed * dt

        self.speed = 0.0
        self.sideSpeed = 0.0
        self.rotationX = ogre.Degree(0.0)
        self.rotationY = ogre.Degree(0.0)
        self.translateVector = ogre.Vector3().ZERO

        self.handleKeyboard(dt)
        self.handleMouse(dt)
        self.handleMiscInput(dt)
        self.handleJoyStick(dt)

        self.moveCamera(dt)

    def handleKeyboard(self, dt):
        if self.keyboard.isKeyDown(OIS.KC_ESCAPE):
            self.engine.stop()


    def handleMouse(self, dt):
        ms = self.mouse.getMouseState()

        if self.toggle < 0 and ms.buttonDown(OIS.MB_Left):
            self.toggle = 0.2
            self.leftMouseClicked(ms, dt)

        if self.missileToggle < 0.0 and ms.buttonDown(OIS.MB_Right):
            self.missileToggle = 5.0
            self.rightMouseClicked(ms, dt)

        #if ms.buttonDown(OIS.MB_Middle):
        self.middleMouseHeld(ms, dt)

    def handleMiscInput(self, dt):
        if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_P):
            if self.soundPlaying:
                self.engine.soundMgr.stop()

            else:
                self.engine.soundMgr.play()

            self.soundPlaying = not self.soundPlaying
            self.toggle = 0.25

        if self.keyboard.isKeyDown(OIS.KC_T):
            print "\n" * 50

        if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_PGUP):
            self.joystickSensitivity += 0.5
            self.toggle = 0.25
            
        if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_PGDOWN):
            if self.joystickSensitivity >= 1.0:
                self.joystickSensitivity -= 0.5
                self.toggle = 0.25    
                

    def leftMouseClicked(self, state, dt, makeSound = True, player_ent = None):
        #player_ent = self.engine.gameMgr.player_ent
        if player_ent is None:
            player_ent = self.engine.gameMgr.player_ent
            
        player_ent.shot = True
        entity = self.engine.entityMgr.createEnt(ent.BULLET, pos = player_ent.pos, orientation = player_ent.orientation)
        
        #print "IN MOUSE!!!!"
        #print self.engine.entityMgr.ents
        self.spawnBullet = True
        #print self.spawnBullet
        #print entity.uiname
        if makeSound:
            self.engine.soundMgr.play('shot')
        '''
        rw = self.engine.gfxMgr.renderWindow
        mouseRay = self.camera.getCameraToViewportRay(state.X.abs / float(rw.getWidth()),
                                                      state.Y.abs / float(rw.getHeight()))
        self.raySceneQuery.setRay(mouseRay)
        self.raySceneQuery.setSortByDistance(True)

        result = self.raySceneQuery.execute()

        for item in result:
            if item.movable:
                if item.movable.getName() == 'GroundEntity' and len(result) == 1:
                    self.engine.selectionMgr.deselectAllEntities()

                elif item.movable.getName() != 'GroundEntity':
                    self.engine.selectionMgr.selectEntityOnClick(item.movable.getName(), self.keyboard.isKeyDown(OIS.KC_LSHIFT))
        '''

    def rightMouseClicked(self, state, dt, player_ent = None, enemy_ent = None):
        if player_ent is None:
            player_ent = self.engine.gameMgr.player_ent
            
        if enemy_ent is None:
            enemy_ent = self.engine.gameMgr.enemy_ent

        entity = self.engine.entityMgr.createEnt(ent.MISSILE, pos = player_ent.pos, orientation = player_ent.orientation)
        entity.commands.append(ai.Intercept(entity, enemy_ent))
        
        self.spawnMissile = True
        
        print enemy_ent.pos
        
        
        
        
        
        
    def middleMouseHeld(self, state, dt):
        self.rotationX = ogre.Degree(- state.X.rel * 0.13)
        self.rotationY = ogre.Degree(- state.Y.rel * 0.13)

    def moveCamera(self, dt):
        #self.translateVector.y = 0
        self.camera.yaw(self.rotationX)
        self.camera.pitch(self.rotationY)
        #self.camera.moveRelative(self.translateVector)

        #ent_id = int(sys.argv[3]) if len(sys.argv) > 3 else 0

        ent = self.engine.gameMgr.player_ent
        #ent.pitch = self.camera.pitch()
        ent.orientation = self.camera.getDirection()
        ent.upVec = self.camera.getUp()

        # if camera_pos.y > 100:
        #     camera_pos.y = 100

        self.camera.setPosition(ent.pos)



    def handleJoyStick(self, dt):
        if not self.joystick:
            return

        #return
        state = self.joystick.getJoyStickState()
        axes = state.mAxes

        max_axis = 32767#self.joystick.MAX_AXIS

        self.speed = -axes[1].abs / float(max_axis)
        self.sideSpeed = -axes[0].abs / float(max_axis)

        yMovement = -axes[4].abs / float(max_axis)
        xMovement = -axes[3].abs / float(max_axis)

        if xMovement > 0.2 or xMovement < -0.2:
            self.rotationX = ogre.Degree(xMovement * self.joystickSensitivity)

        if yMovement > 0.2 or yMovement < -0.2:
            self.rotationY = ogre.Degree(yMovement * self.joystickSensitivity)

        if axes[5].abs / float(max_axis) > 0.2 and self.toggle < 0:
            self.toggle = 0.25
            self.leftMouseClicked(None,dt)
            
        elif axes[2].abs / float(max_axis) > 0.2 and self.missileToggle < 0:
            self.missileToggle = 5.0
            self.rightMouseClicked(None,dt)
            
