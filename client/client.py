import socket

class Client:
    def __init__(self, host, port):
        self.sock = socket.socket()
        self.sock.connect((host, port))

    def login(self):
        username = input('username:')
        password = input('password:')
        # TODO enviar credenciais
        self.sock.send()

client = Client('localhost', 9999)
