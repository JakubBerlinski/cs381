# 381 main engine

class Engine(object):
    '''
    The root of the global manager tree
    '''

    def __init__(self):
        pass

    def init(self):
        import entityMgr
        self.entityMgr = entityMgr.EntityMgr(self)
        self.entityMgr.init()
        self.keepRunning = True;

        import gfxMgr
        self.gfxMgr = gfxMgr.GfxMgr(self)
        self.gfxMgr.init()

        import netMgr
        self.netMgr = netMgr.NetMgr(self)
        self.netMgr.init()

        import inputMgr
        self.inputMgr = inputMgr.InputMgr(self)
        self.inputMgr.init()

        import selectionMgr
        self.selectionMgr = selectionMgr.SelectionMgr(self)
        self.selectionMgr.init()

        import controlMgr
        self.controlMgr = controlMgr.ControlMgr(self)
        self.controlMgr.init()

        import soundMgr
        self.soundMgr = soundMgr.SoundManager(self)
        self.soundMgr.init()

        import gameMgr
        self.gameMgr = gameMgr.GameMgr(self)
        self.gameMgr.init()

        import overlayMgr
        self.overlayMgr = overlayMgr.OverlayMgr(self)
        self.overlayMgr.init()


    def stop(self):
        self.gfxMgr.stop()
        self.inputMgr.stop()
        self.selectionMgr.stop()
        self.gameMgr.stop()
        self.controlMgr.stop()
        self.netMgr.stop()
        self.soundMgr.stop('ENGINE_STOP')
        self.overlayMgr.stop()

        print "381 Engine exiting..."
        import sys
        sys.exit()

    def run(self):
        import time, sys
        import ogre.renderer.OGRE as ogre

        isWindows = sys.platform == 'win32'

        weu = ogre.WindowEventUtilities()
        weu.messagePump()

        self.gameMgr.displayStartSplash(0)
        self.soundMgr.play('background')
        
        self.oldTime = time.clock() if isWindows else time.time()
        self.runTime = 0
        while self.keepRunning:
            now = time.clock() if isWindows else time.time()
            dtime = now - self.oldTime
            self.oldTime = now

            self.entityMgr.tick(dtime)
            self.gfxMgr.tick(dtime)
            self.inputMgr.tick(dtime)
            self.netMgr.tick(dtime)
            self.selectionMgr.tick(dtime)
            self.controlMgr.tick(dtime)
            self.gameMgr.tick(dtime)
            self.overlayMgr.tick(dtime)

            self.runTime += dtime

            weu.messagePump()

            time.sleep(0.001)

