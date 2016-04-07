from pickle import dumps, loads
from socket import socket
from sys import getsizeof
from message import Message


class Client:
    def __init__(self, address):
        self.sock = socket()
        self.sock.connect(address)
        self.token = None

    def do_login(self, login, password):
        self.send_message('login', (login, password))
        response = self.recv_message()

    def do_signup(self, name, login, password):
        self.send_message('signup', (name, login, password))
        print(self.recv_message().data)

    def do_sync(self):
        self.send_message('sync', '')

    def recv_message(self):
        return loads(self.sock.recv(getsizeof(Message)))

    def send_message(self, msg_type, data):
        self.sock.sendall(dumps(Message(msg_type, data)))

client = Client(('localhost', 9990))
client.do_signup('bledson', 'bled', '1234')
