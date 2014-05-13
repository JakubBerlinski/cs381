
import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS

class OverlayMgr(object):
    def __init__(self, engine):
        self.engine = engine

    def init(self):
        self.ogreOverlay = ogre.OverlayManager.getSingletonPtr()
        self.numPanels = 0
        self.numLabels = 0
        self.overlays = []
        self.panels = []
        self.labels = []

        self.fontMgr = ogre.FontManager.getSingletonPtr()
        self.fontMgr.load("BlueHighway", ogre.ResourceGroupManager.AUTODETECT_RESOURCE_GROUP_NAME)
        #font = self.fontMgr.getByName("BlueHighway")
        #font.setType(ogre.FT_TRUETYPE)
        #font.setParameter('size', '42')
        #font.reload()
        #font.reload()

        rw = self.engine.gfxMgr.renderWindow
        x = rw.getWidth() / 2.0
        y = rw.getHeight() / 2.0
        self.addPanel(pos = (x - 49.0 ,y - 49.0), material = 'CrossHair')
        self.addPanel(pos = (10,13), dim = (240,35), material = 'Panel/Metal')
        self.addPanel(pos = (10,50), dim = (240,35), material = 'Panel/Metal')
        self.addLabel("Player Health: ", 1, dim = (100,32))
        self.addLabel("Enemy Health: ", 2, dim = (100,32))
        
        self.addPanel(pos = (10,120), dim = (240,35), material = 'Panel/Metal')
        self.addLabel('Bomb Timer: ', 3, dim = (100,32))
        
        self.addPanel(pos = (10,87), dim = (240,35), material = 'Panel/Metal')
        self.addLabel('Sensitivity: ', 4, dim = (100,32))
        
    def tick(self,dt):
        self.labels[0].setCaption('Player Health: ' + str(self.engine.gameMgr.player_ent.health))
        self.labels[1].setCaption('Enemy Health: ' + str(self.engine.gameMgr.enemy_ent.health))
        
        if self.engine.inputMgr.missileToggle < 0.0:
            self.labels[2].setCaption('Bomb Timer: Fire')
            
        else:
            self.labels[2].setCaption('Bomb Timer: ' + '%.1f' %self.engine.inputMgr.missileToggle)
            
        self.labels[3].setCaption('Sensitivity: ' + str(self.engine.inputMgr.joystickSensitivity))
    
    def addPanel(self, pos = (0.0,0.0), dim = (100,100), material = None):
        name = 'panel' + str(self.numPanels)

        overlay = self.ogreOverlay.create(name)
        panel = self.ogreOverlay.createOverlayElement("Panel", name)
        panel.setMetricsMode(ogre.GMM_PIXELS)
        panel.setPosition(*pos)
        panel.setDimensions(*dim)

        if material:
            panel.setMaterialName(material)

        panel.show()
        overlay.add2D(panel)
        overlay.show()

        self.panels.append(panel)
        self.overlays.append(overlay)

        self.numPanels += 1

        return panel

    def addLabel(self, text = 'LABEL', panel = None, pos = (0.0,0.0), dim = (100,13), color = (1.0,1.0,0.7)):
        name = 'label' + str(self.numLabels)

        textArea = self.ogreOverlay.createOverlayElement("TextArea", name)
        textArea.setMetricsMode(ogre.GMM_PIXELS)
        textArea.setCaption(text)
        textArea.setPosition(pos[0]+5, pos[1]+5)
        textArea.setDimensions(*dim)
        textArea.setFontName("BlueHighway")
        textArea.setCharHeight(dim[1])
        textArea.setColour(color)

        if isinstance(panel, int):
            self.panels[panel].addChild(textArea)

        elif isinstance(panel, ogre.PanelOverlayElement):
            panel.addChild(textArea)

        else:
            if len(self.panels) > 0:
                self.panels[-1].addChild(textArea)

        self.labels.append(textArea)
        self.numLabels += 1

        return textArea

    def hidePanel(self, panel):
        self.panels[panel].hide()

    def showPanel(self, panel):
        self.panels[panel].show()

    def stop(self):
        self.fontMgr.unloadAll(False)
