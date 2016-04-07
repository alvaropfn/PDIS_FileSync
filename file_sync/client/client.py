import pickle
import socket
import time

from file_sync.message import Message


class Client:
    def __init__(self, host, port):
        self.sock = socket.socket()
        self.sock.connect((host, port))

    def __del__(self):
        self.sock.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()

    def login(self):
        username = 'login'#input('username: ')
        password = 'senha'#input('password: ')
        msg = pickle.dumps(Message('login', (username, password)))
        # TODO enviar credenciais
        self.sock.send(msg)
        print(self.sock.recv(1024))

client = Client('localhost', 9999)
client.login()
