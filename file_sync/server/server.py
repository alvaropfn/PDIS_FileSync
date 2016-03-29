import socket
from file_sync.server.handler import Handler


class Server:
    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind(('localhost', 9999))
        self.sock.listen(2)
        while True:
            client_socket, address = self.sock.accept()
            handler = Handler(client_socket, address)
            handler.run()

    def __del__(self):
        self.sock.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()

server = Server()
