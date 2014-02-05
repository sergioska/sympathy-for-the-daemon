__author__ = 'sergioska'

""" currently this class is not used!!! """

import SocketServer

class TCPHandler:

    def handle(self):
        self.data = self.rfile.readline().strip()
        print "{} wrote: " . format(self.client_address[0])
        print self.data
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 6666

server = SocketServer.TCPServer((HOST, PORT), TCPHandler)
server.serve_forever()


