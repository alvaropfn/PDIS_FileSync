import random
import sqlite3
import string
from message import Message


class UserManager:
    def __init__(self):
        self.connection = sqlite3.connect(r'users.db')
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def check_user(self, login, password):
        user = self.cursor.execute('''SELECT *
            FROM users
            WHERE login = ?''', login).fetchone()
        if user is not None:
            if user[3] == password:
                return Message('response', 'User exists')
            else:
                return Message('response',
                               'Users exists. Check password')
        else:
            return Message('response', 'User does not exists')

    def create_user(self, name, login, password):
        try:
            self.cursor.execute('''INSERT INTO users(name, login, pwd)
                                VALUES(?, ?, ?)''', (name, login, password))
            self.connection.commit()
            return Message('response', 'User created')
        except sqlite3.Error as e:
            return Message('response', 'Could not create user. ' + e.args[0])

    def create_token(self, login, password):
        user = self.cursor.execute('''SELECT *
            FROM users
            WHERE login = ? AND pwd = ?''', (login, password)).fetchone()
        if user is not None:
            ''.join(random.SystemRandom()
                    .choice(string.ascii_letters + string.digits))
        else:
            return Message('response',
                           'Could not create token. Check login or password.')

    def is_valid_token(self, token):
        # TODO checar se token é válido
        user = self.cursor.execute('''SELECT *
            FROM users
            WHERE token = ?''', token).fetchone()
        pass
