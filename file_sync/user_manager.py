import datetime
import random
import sqlite3
import string
from file_sync.message import Message


class UserManager:
    def __init__(self):
        self.connection = sqlite3.connect(r'users.db',
                                          detect_types=sqlite3.PARSE_DECLTYPES)
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
        token = ''.join(random.SystemRandom()
                        .choice(string.ascii_letters + string.digits)
                        for _ in range(29))
        try:
            self.cursor.execute('''INSERT INTO users (name, login, pwd, token)
                                VALUES (?, ?, ?, ?)''', (name, login, password, token))
            self.connection.commit()
            return Message('response', 'User created')
        except sqlite3.Error as e:
            return Message('response', 'Could not create user. ' + e.args[0])

    def create_token(self, login, password):
        user = self.cursor.execute('''SELECT *
            FROM users
            WHERE login = ? AND pwd = ?''', (login, password)).fetchone()
        if user is not None:
            token = ''.join(random.SystemRandom()
                            .choice(string.ascii_letters + string.digits)
                            for _ in range(30))
            try:
                self.cursor.execute('''UPDATE users
                    SET token=? AND expiry_date=? WHERE login=?''',
                                    (token,
                                     datetime.datetime.now(), login))
                self.connection.commit()
            except sqlite3.Error as e:
                print(e.args[0])
        else:
            return Message('response',
                           'Could not create token. Check login or password.')

    def is_valid_token(self, token):
        # TODO checar se token é válido
        user = self.cursor.execute('''SELECT *
            FROM users
            WHERE token = ?''', token).fetchone()
        pass


user_manager = UserManager()
user_manager.create_user('bledson', 'bled', '1234')
user_manager.create_token('bled', '1234')
