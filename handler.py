import socket
import threading

class Handler(threading.Thread):
    def __init__(self, conn: socket.socket, addr):
        super().__init__()
        self.CONN = conn
        self.ADDR = addr

    def run(self):
        self.CONN.send('Hello World!'.encode())
