
try:
    import ogre.sound.OgreAL as ogreS
    from ogre.renderer.OGRE import OgreException
    
    class SoundManager(object):
        def __init__(self, engine):
            self.engine = engine
            #self.engine.gfxMgr.root.loadPlugin("OgreOggSound")
            #self.manager = ogreS.OgreOggSoundManager.getSingletonPtr()
            self.manager = ogreS.SoundManager()
            #self.manager
            self.sounds = []
            print self.manager

        def init(self):
            self.addSound('background', 'background.ogg', True)
            #self.play('background')
            self.addSound('shot', 'gun-shot.ogg', False)
            self.addSound('blast', 'blast.ogg', False)
            self.addSound('win', 'win.ogg', False)
            self.addSound('lose', 'lose.ogg', False)

        def addSound(self, soundName, soundFile, isMusic = False):
            try:
                sound = self.manager.createSound(soundName, soundFile, isMusic, True)
                sound.setGain(0.2)
                self.sounds.append((soundName, sound))
            except OgreException:
                print "%s Unable to load sound file: %s %s" % ('#' * 10, soundFile, '#' * 10)
                print "%s Skipping... %s" % ('#' * 10, '#' * 10)

        #def getSound(self, soundName):
            #return self.manager.getSound(soundName)

        def play(self, soundName = ''):
            if soundName == '':
                for sound in self.sounds:
                    sound[1].play()

            else:
                self.stop(soundName)
                for sound in self.sounds:
                    if sound[0] == soundName:
                        sound[1].play()

        def pause(self, soundName = ''):
            if soundName == '':
                for sound in self.sounds:
                    self.manager.getSound(sound).pause()

            else:
                self.manager.getSound(soundName).pause()

        def stop(self, soundName = ''):
            if soundName == '':
                for sound in self.sounds:
                    sound[1].stop()
                    
            elif soundName == 'ENGINE_STOP':
                for sound in self.sounds:
                    try:
                        self.manager.destroySound(sound[1])
                        
                    except:
                        pass
                    

            else:
                for sound in self.sounds:
                    if sound[0] == soundName:
                        sound[1].stop()
                

except ImportError:
    print "NO SOUND"
    class SoundManager(object):
        def __init__(self, engine):
            pass

        def init(self):
            pass

        def addSound(self, soundName, soundFile, isMusic = False):
            pass

        def getSound(self, soundName):
            pass

        def play(self, soundName = ''):
            pass

        def pause(self, soundName = ''):
            pass

        def stop(self, soundName = ''):
            pass
            
