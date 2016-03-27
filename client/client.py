import socket

class Client:
    def __init__(self, host, port):
        self.sock = socket.socket()
        self.sock.connect((host, port))
        print(self.sock.recv(1024))

    def login(self):
        username = input('username:')
        password = input('password:')
        self.sock.send()

client = Client(socket.gethostname(), 9999)
