
import ogre.io.OIS as OIS

class ControlMgr(object):
    def __init__(self, engine):
        self.engine = engine
        
    def init(self):
        self.keyboard = self.engine.inputMgr.keyboard

    def stop(self):
        pass
        
    def tick(self, dt):
        player_ent = self.engine.gameMgr.player_ent

        if self.keyboard.isKeyDown(OIS.KC_W):
            player_ent.speed = player_ent.maxSpeed

        elif self.keyboard.isKeyDown(OIS.KC_S):
            player_ent.speed = -player_ent.maxSpeed

        else:
            player_ent.speed = 0


        if self.keyboard.isKeyDown(OIS.KC_A):
            player_ent.sideSpeed = player_ent.maxSpeed

        elif self.keyboard.isKeyDown(OIS.KC_D):
            player_ent.sideSpeed = -player_ent.maxSpeed

        else:
            player_ent.sideSpeed = 0


        if self.keyboard.isKeyDown(OIS.KC_R) or self.engine.inputMgr.moveUp:
            player_ent.upSpeed = player_ent.maxSpeed

        elif self.keyboard.isKeyDown(OIS.KC_F) or self.engine.inputMgr.moveDown:
            player_ent.upSpeed = -player_ent.maxSpeed

        else:
            player_ent.upSpeed = 0


        speed = self.engine.inputMgr.speed
        sideSpeed = self.engine.inputMgr.sideSpeed

        if speed > 0.15:
            player_ent.speed = speed * player_ent.maxSpeed

        elif speed < -0.15:
            player_ent.speed = speed * player_ent.maxSpeed


        if sideSpeed > 0.15:
            player_ent.sideSpeed = sideSpeed * player_ent.maxSpeed

        elif sideSpeed < -0.15:
            player_ent.sideSpeed = sideSpeed * player_ent.maxSpeed

        '''
        for ent in self.engine.selectionMgr.selectedEntities:
            if self.keyboard.isKeyDown(OIS.KC_UP):
                if ent.speed < ent.maxSpeed:
                    ent.speed += 1

            if self.keyboard.isKeyDown(OIS.KC_DOWN):
                if ent.speed > -ent.maxSpeed:
                    ent.speed -= 1

            if self.keyboard.isKeyDown(OIS.KC_LEFT):
            	pass
                # ent.desiredHeading -= 1

            if self.keyboard.isKeyDown(OIS.KC_RIGHT):
            	pass
                # ent.desiredHeading += 1

            if self.keyboard.isKeyDown(OIS.KC_SPACE):
            	pass
                # ent.desiredSpeed = 0
                # ent.desiredHeading = ent.heading
                # ent.commands = []

        '''
