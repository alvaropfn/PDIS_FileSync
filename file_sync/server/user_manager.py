import sqlite3


class UserManager:
    def __init__(self):
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS USERS(
            ID INT PRIMARY KEY AUTOINCREMENT,
            NAME TEXT NOT NULL UNIQUE,
            PWD TEXT NOT NULL)''')
        self.connection.commit()

    def check_user(self, username, password):
        user = self.cursor.execute('''SELECT *
            FROM USERS
            WHERE NAME = ? AND PWD = ?''', (username, password)).fetchone()
        if user is not None:
            return True
        else:
            return False

    def create_user(self, username, password):
        try:
            self.cursor.execute('INSERT INTO USERS(NAME, PWD) VALUES(?, ?)',
                                (username, password))
            return 'User created'
        except sqlite3.Error as e:
            return 'Could not create user. ' + e.args[0]


usermanager = UserManager()
