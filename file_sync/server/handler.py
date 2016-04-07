import pickle
from socket import socket
import sys
from threading import Thread
from file_sync.message import Message


class Handler(Thread):
    def __init__(self, client: socket, address):
        super().__init__()
        self.sock = client
        self.addr = address

    def __del__(self):
        self.sock.close()

    def run(self):
        b = pickle.loads(self.sock.recv(sys.getsizeof(Message, 1024)))
        self.sock.send('Hello World!'.encode())
