import sys, socket, threading

class GameServer(object):
    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname()) if len(sys.argv) < 2 else sys.argv[1]
        self.port = 1111
        self.connections = []

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.ip, self.port))

        print 'Server created: (%s, %d)' % (self.ip, self.port)

    def run(self):
        try:
            while True:
                raw_data, address = self.socket.recvfrom(1024)
                if address not in self.connections:
                    self.connections.append(address)
                    self.create_client_thread(address)

        except KeyboardInterrupt:
            print '\nServer Shutting Down...'
            sys.exit()


    def create_client_thread(self, clientAddr):
        self.port += 1
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(3.0)
        while True:
            try:
                sock.bind((self.ip, self.port))
                break
            except socket.error:
                self.port += 1

        message = str(self.port)
        sock.sendto(message, clientAddr)
        data, address = sock.recvfrom(1024)
        print 'Connection Established:', address

        thread = threading.Thread(target=self.handle_client, args=(sock,clientAddr))
        thread.daemon = True
        thread.start()

    def handle_client(self, sock, clientAddr):
        try:
            while True:
                data, address = sock.recvfrom(2048)

                for addr in self.connections:
                    if addr != address:
                        sock.sendto(data, addr)

        except socket.timeout:
            print 'Socket Timeout occured, disconnecting:', clientAddr
            sock.close()
            
            i = 0
            for addr in self.connections:
                if addr == clientAddr:
                    break
                    
                i += 1
                
            del self.connections[i]


if __name__ == '__main__':
    server = GameServer()
    server.run()
