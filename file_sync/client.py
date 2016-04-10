from pickle import dumps, loads
from socket import socket
from sys import getsizeof

from file_sync.message import Message


class Client:
    """Classe cliente"""

    def __init__(self, address):
        """Construtor
        :param address: endereço para conexão
        """
        self.sock = socket()
        self.sock.connect(address)
        self.token = None

    def do_login(self, login, password):
        """Requisita login no servidor
        :param login: nome de usuario no servidor
        :param password: senha no servidor
        """
        self.send_message('login', (login, password))
        response = self.recv_message()
        self.token = response.data

    def do_signup(self, name, login, password):
        """Requisita cadastro no servidor
        :param name: nome do cliente
        :param login: nome de usuario
        :param password: senha do usuario
        """
        self.send_message('signup', (name, login, password))
        print(self.recv_message().data)

    def do_sync(self):
        """Requisita sincronização"""
        self.send_message('sync', '')

    def recv_message(self):
        """Utilidade. Deserializa objeto Message recebido via socket"""
        return loads(self.sock.recv(getsizeof(Message, 1024)))

    def send_message(self, msg_type, data):
        """Utilidade. Serializa e envia objeto Message via socket
        :param msg_type: tipo da mensagem
        :param data: conteudo da mensagem
        """
        self.sock.sendall(dumps(Message(msg_type, data)))


client = Client(('localhost', 9990))
client.do_signup('bledson', 'bled', '1234')
