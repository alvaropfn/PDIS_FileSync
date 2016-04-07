from pickle import dumps, loads
from socketserver import BaseRequestHandler, ThreadingTCPServer
from sys import getsizeof
from file_sync.message import Message
from file_sync.user_manager import UserManager


class Handler(BaseRequestHandler):
    """Classe para controlar as requisições ao servidor"""

    def handle(self):
        """Método principal. Sobrepõe o método da classe-base"""

        message = loads(self.request.recv(getsizeof(Message)))
        if message is None:
            self.request.sendall(Message('reply', 'No message received'))
        elif message.msg_type == 'signup':
            self.signup(message)

    def login(self, message):
        """Método para gerenciar login"""

        user_manager = UserManager()
        login, password = message.data
        response = user_manager.check_user(login, password)
        # TODO salvar token e tempo de expiração
        if response.data == 'User exists':
            pass
        elif response.data == 'Users exists. Check password':
            pass
        else:
            self.request.sendall(dumps(response))

    def signup(self, message):
        """Método para gerenciar cadastro"""
        user_manager = UserManager()
        name, login, password = message.data
        response = user_manager.create_user(name, login, password)
        self.request.sendall(dumps(response))


serv = ThreadingTCPServer(('localhost', 9990), Handler, True)
serv.serve_forever()
