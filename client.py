import socket
import time


class Client:
    def __init__(self, host, port):
        self.SOCKET = socket.socket()
        self.SOCKET.connect((host, port))
        print(self.SOCKET.recv(1024))
        time.sleep(30)

client = Client(socket.gethostname(), 9990)
