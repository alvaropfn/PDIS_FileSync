import sqlite3


class UserManager:
    def __init__(self):
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS USERS(
            ID INT PRIMARY KEY,
            NAME TEXT NOT NULL UNIQUE,
            PWD TEXT NOT NULL)''')
        self.connection.commit()

    def check_user(self, username, password):
        user = self.cursor.execute('SELECT * FROM USERS WHERE NAME = ? AND PWD = ?', (username, password)).fetchone()
        if (user != None):
            print('existe')
        else:
            print('nao existe')


usermanager = UserManager()
usermanager.check_user('nome', 'senha')
