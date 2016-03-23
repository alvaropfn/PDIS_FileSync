import socket
from handler import Handler


class Server:
    def __init__(self):
        self.SOCKET = socket.socket()
        self.SOCKET.bind((socket.gethostname(), 9990))
        self.SOCKET.listen(2)
        while True:
            conn, addr = self.SOCKET.accept()
            handler = Handler(conn, addr)
            handler.start()

server = Server()
