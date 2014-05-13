# Networking manager.
import ogre.renderer.OGRE as ogre
import sys, socket, threading
import cPickle as pickle
import ent as ents

class NetMgr(object):
    def __init__(self, engine):
        self.engine = engine
        self.running = True
        self.time = 0.0

    def init(self):
        self.server_ip = sys.argv[1] if len(sys.argv) > 1 else None

        if self.server_ip is None:
            return

        self.ip = socket.gethostbyname(socket.gethostname()) if len(sys.argv) < 3 else sys.argv[2]
        self.port = 1111
        self.server_port = 1111
        self.server_data = {}
        self.server_addr = (self.server_ip, self.server_port)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        while True:
            try:
                self.socket.bind((self.ip, self.port))
                break
            except socket.error:
                self.port += 1

        print "NET: Server IP: %s, port: %d, local IP: %s, local port: %d" % (self.server_ip, self.server_port, self.ip, self.port)

        print 'NET: Connecting to server...'

        self.socket.sendto('connect', self.server_addr)
        newport, addr = self.socket.recvfrom(1024)
        self.server_port = int(newport)
        self.server_addr = (self.server_ip, self.server_port)
        self.socket.sendto('connected', self.server_addr)

        #self.get_data()

        self.socket_thread = threading.Thread(target=self.get_data)
        self.socket_thread.daemon = True
        self.socket_thread.start()
        #self.socket.sendto(pickle.dumps('This is a test string'), (self.server_ip, self.server_port))


    def tick(self, dt):
        if self.server_ip is None:
            return

        self.time += dt
        send_data = {}
        for ent in self.engine.entityMgr.ents.values():
            if isinstance(ent, ents.DRONE):
                quat = (ent.quaternion.w, ent.quaternion.x, ent.quaternion.y, ent.quaternion.z)
                send_data[ent.id] = [(ent.pos.x, ent.pos.y, ent.pos.z), ent.speed, (ent.orientation.x, ent.orientation.y, ent.orientation.z), ent.upSpeed, ent.sideSpeed, ent.health, self.engine.inputMgr.spawnBullet, self.engine.inputMgr.spawnMissile, quat]
            
        send_data = pickle.dumps(send_data, pickle.HIGHEST_PROTOCOL)
        self.socket.sendto(send_data, self.server_addr)

        for key in self.server_data:
            try:
                if self.time > 5.0:
                    new_pos = self.server_data[key][0]
                    new_pos = ogre.Vector3(new_pos[0], new_pos[1], new_pos[2])
                    self.engine.entityMgr.ents[key].pos = new_pos

                new_speed = self.server_data[key][1]
                new_orientation = self.server_data[key][2]
                new_orientation = ogre.Vector3(new_orientation[0], new_orientation[1], new_orientation[2])
                new_upSpeed = self.server_data[key][3]
                new_sideSpeed = self.server_data[key][4]
                
                self.engine.entityMgr.ents[key].speed = new_speed
                self.engine.entityMgr.ents[key].orientation = new_orientation
                self.engine.entityMgr.ents[key].upSpeed = new_upSpeed
                self.engine.entityMgr.ents[key].sideSpeed = new_sideSpeed
                if self.server_data[key][5] < self.engine.entityMgr.ents[key].health:
                    self.engine.entityMgr.ents[key].health = self.server_data[key][5]
                
                if self.server_data[key][6]:
                    self.engine.inputMgr.leftMouseClicked(None,dt,False, self.engine.gameMgr.enemy_ent)
                    
                if self.server_data[key][7]:
                    self.engine.inputMgr.rightMouseClicked(None,dt, self.engine.gameMgr.enemy_ent, self.engine.gameMgr.player_ent)
                    
                quat = self.server_data[key][8]
                self.engine.entityMgr.ents[key].quaternion = ogre.Quaternion(quat[0],quat[1],quat[2],quat[3])
            except:
                pass

        if self.time > 5.0:
            self.time = 0.0
            
    def stop(self):
        self.running = False
        #self.socket_thread.join()

    def get_data(self):
        while self.running:
            raw_data, server_addr = self.socket.recvfrom(5120)
            self.server_data = pickle.loads(raw_data)


