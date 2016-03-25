import sqlite3


class UserManager:
    def __init__(self):
        self.CURSOR = sqlite3.connect(":memory:").cursor()
        self.CURSOR.execute('''CREATE TABLE USERS(
            ID INT PRIMARY KEY,NAME TEXT NOT NULL,
            PWD TEXT NOT NULL)''')

usermanager = UserManager()
