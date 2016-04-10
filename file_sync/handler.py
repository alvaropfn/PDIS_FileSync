from pickle import dumps, loads
from socketserver import BaseRequestHandler, ThreadingTCPServer
from sys import getsizeof

from file_sync.message import Message
from file_sync.user_manager import UserManager


class Handler(BaseRequestHandler):
    """Classe para controle de requisições ao servidor"""

    def handle(self):
        """Analisa e responde requisição
        de acordo com o msg_type de Message"""

        message = loads(self.request.recv(getsizeof(Message, 1024)))
        if message is None:
            self.request.sendall(Message('reply', 'No message received'))
        elif message.msg_type == 'signup':
            self.signup(message)

    def login(self, message):
        """Realiza login de clientes
        :param message: mensagem do cliente
        """

        user_manager = UserManager()
        login, password = message.data
        response = user_manager.check_user(login, password)
        if response.data[0] == 'User exists':
            response.data = response.data[1]
        else:
            self.request.sendall(dumps(response))

    def signup(self, message):
        """Realiza cadastro de clientes
        :param message: mensagem do cliente
        """
        user_manager = UserManager()
        name, login, password = message.data
        response = user_manager.create_user(name, login, password)
        self.request.sendall(dumps(response))


serv = ThreadingTCPServer(('localhost', 9990), Handler, True)
serv.serve_forever()
