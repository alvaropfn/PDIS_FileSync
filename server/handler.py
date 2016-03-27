import socket
import threading

class Handler(threading.Thread):
    def __init__(self, client: socket.socket, address):
        super().__init__()
        self.CONN = client
        self.ADDR = address

    def run(self):
        self.CONN.send('Hello World!'.encode())
