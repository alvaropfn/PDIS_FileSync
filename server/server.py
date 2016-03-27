import socket
from server.handler import Handler
from server.user_manager import UserManager


class Server:
    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind(('localhost', 9999))
        self.sock.listen(2)
        while True:
            client_socket, address = self.sock.accept()
            handler = Handler(client_socket, address)
            handler.run()

server = Server()
