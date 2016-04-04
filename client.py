import socket
import time


class Client:
    def __init__(self, host, port):
        self.SOCKET = socket.socket()
        self.SOCKET.connect((host, port))
        time.sleep(30)
        print(self.SOCKET.recv(1024))

client = Client(socket.gethostname(), 9990)