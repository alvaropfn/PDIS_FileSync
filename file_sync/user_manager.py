import random
import sqlite3
import string

from file_sync.message import Message


class UserManager:
    """Classe para gerenciar persistência"""

    def __init__(self):
        self.connection = sqlite3.connect(r'users.db')
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def check_user(self, login, password):
        """Verifica se usuario existe no BD
        :param login: nome de usuario a ser verificado
        :param password: senha de usuario a ser verificado
        """
        user = self.cursor.execute(
            '''SELECT * FROM users WHERE login = ?''', login).fetchone()
        if user is not None:
            if user[3] == password:
                return Message('response', 'User exists')
            else:
                return Message('response',
                               'Users exists. Check password')
        else:
            return Message('response', 'User does not exists')

    def create_user(self, name, login, password):
        """Insere novo usuario no BD
        :param name: nome do cliente
        :param login: nome do usuario
        :param password: senha do usuario
        """
        try:
            self.cursor.execute(
                '''INSERT INTO users(name, login, pwd) VALUES(?, ?, ?)''',
                (name, login, password))
            self.connection.commit()
            return Message('response', 'User created')
        except sqlite3.Error as e:
            return Message('response', 'Could not create user. ' + e.args[0])

    def create_token(self, login, password):
        """Cria código verificador (token) para um usuario
        Validade padrão do token é de 50min
        :param login: nome do usuario
        :param password: senha do usuario
        """
        user = self.cursor.execute(
            '''SELECT * FROM users WHERE login = ? AND pwd = ?''',
            (login, password)).fetchone()
        if user is not None:
            ''.join(random.SystemRandom().choice(
                string.ascii_letters + string.digits))
        else:
            return Message('response',
                           'Could not create token. Check login or password.')

    def is_valid_token(self, token):
        """Checa se código verificador (token) é válido
        :param token: código verificador a ser validado
        """
        # TODO checar se token é válido
        user = self.cursor.execute(
            '''SELECT * FROM users WHERE token = ?''', token).fetchone()
        pass
