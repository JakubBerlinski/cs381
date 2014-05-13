import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import ent, sys, time

Vector3 = ogre.Vector3

class GameMgr:
    def __init__(self, engine):
        self.engine = engine
        print "starting Game mgr"
        pass

    def init(self):
        self.loadLevel()

    def stop(self):
        pass

    def loadLevel(self):
        self.game1()


    def game1(self):
        ent_id = int(sys.argv[3]) - 1 if len(sys.argv) > 3 else 0

        if ent_id == 0:
            self.player_ent = self.engine.entityMgr.createEnt(ent.DRONE, pos = Vector3(-50,10,0))
            self.enemy_ent = self.engine.entityMgr.createEnt(ent.DRONE, pos = Vector3(50,10,0))

        else:
            self.enemy_ent = self.engine.entityMgr.createEnt(ent.DRONE, pos = Vector3(-50,10,0))
            self.player_ent = self.engine.entityMgr.createEnt(ent.DRONE, pos = Vector3(50,10,0))
            
        
        # self.engine.entityMgr.createEnt(ent.WALL, pos = Vector3(100,0,0), yaw = 0)
        # self.engine.entityMgr.createEnt(ent.WALL, pos = Vector3(-100,0,0), yaw = 0)
        # self.engine.entityMgr.createEnt(ent.WALL, pos = Vector3(0,0,100), yaw = 100)
        # self.engine.entityMgr.createEnt(ent.WALL, pos = Vector3(0,0,-100), yaw = 100)


    def tick(self, dt):
        if self.enemy_ent.health <= 0:
            self.displayEndSplash(True, dt)

        elif self.player_ent.health <= 0:
            self.displayEndSplash(False, dt)


    def displayStartSplash(self, dt):
        rw = self.engine.gfxMgr.renderWindow
        overlayMgr = self.engine.overlayMgr
        panel = overlayMgr.addPanel(pos=(0,0), dim=(rw.getWidth(),rw.getHeight()), material = 'SplashScreen')
        for i in range(5):
            overlayMgr.hidePanel(i)
        #overlayMgr.tick(dt)
        self.engine.gfxMgr.tick(dt)

        while not self.engine.inputMgr.keyboard.isKeyDown(OIS.KC_SPACE):
            self.engine.netMgr.tick(dt)
            self.engine.inputMgr.keyboard.capture()

        panel.hide()
        
        self.displayIntroScreen(dt)
        
    def displayEndSplash(self, win, dt):
        credits = '''
        Cameron Rowe -- Networking, Physics, AI, GamePad\n
        Jakub Berlinski -- Physics, AI, Graphics, Collisions'''
        rw = self.engine.gfxMgr.renderWindow
        if win:
            text = 'You Won'
            self.engine.soundMgr.play('win')
            
        else:
            text = 'You Lost'
            self.engine.soundMgr.play('lose')
            
        overlayMgr = self.engine.overlayMgr
        overlayMgr.tick(dt)
        pos = (0,0)
        panel = overlayMgr.addPanel(pos=pos, dim=(rw.getWidth(),rw.getHeight()), material = 'Panel/Metal')
        pos = (rw.getWidth()/2.0 - 100,rw.getHeight() / 2.0 - 60)
        overlayMgr.addLabel(text, panel, pos, (100,65), (1,1,0))
        pos = (25 ,rw.getHeight() / 2.0 - 20)
        overlayMgr.addLabel(credits, panel, pos, (100,65), (1,1,0))
        overlayMgr.hidePanel(0)

        #overlayMgr.tick(dt)
        self.engine.gfxMgr.tick(dt)

        self.engine.inputMgr.keyboard.capture()
        while not self.engine.inputMgr.keyboard.isKeyDown(OIS.KC_SPACE):
            self.engine.inputMgr.keyboard.capture()

        #overlayMgr.showPanel(0)
        panel.hide()

        self.engine.stop()


    def displayIntroScreen(self, dt):
        text = '''
        Movement:\n
        Up/Down Movement:\n
        Shoot:\n
        Tracking Bombs:\n
        Play / Pause Music:\n
        Change Controller Sensitivity:\n
        Quit:'''
        rw = self.engine.gfxMgr.renderWindow
        overlayMgr = self.engine.overlayMgr
        pos = (0,0)
        panel = overlayMgr.addPanel(pos=pos, dim=(rw.getWidth(),rw.getHeight()), material = 'Panel/Metal')
        pos = (0,0)
        overlayMgr.addLabel(text, panel, pos, (100,65), (1,1,0))
        
        pos = (800,0)
        text = '''
        W,A,S,D OR Left Thumbstick\n
        R,F\n
        Left Click OR Right Trigger\n
        Right Click OR Left Trigger\n
        P\n
        PGUP, PGDOWN\n
        Escape'''
        overlayMgr.addLabel(text, panel, pos, (100,65), (1,1,0))
        
        pos = (700,980)
        text = 'Press Space to Start'
        overlayMgr.addLabel(text,panel,pos, (100,65), (1,1,0))        

        self.engine.gfxMgr.tick(dt)

        time.sleep(2)
        self.engine.inputMgr.keyboard.capture()
        while not self.engine.inputMgr.keyboard.isKeyDown(OIS.KC_SPACE):
            self.engine.inputMgr.keyboard.capture()
            self.engine.netMgr.tick(dt)
            

        for i in range(5):
            overlayMgr.showPanel(i)
        panel.hide()
