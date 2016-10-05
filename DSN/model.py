__author__ = 'Girish'

import sqlite3
import os.path
from contextlib import closing

class Database(object):

    def __init__(self,app):
        self.app = app
        self.db_path = os.path.join(self.app.config["ROOT"],self.app.config["DATABASE"])

    def init_db(self):
        if os.path.exists(self.db_path):
            return
        with closing(self.connect_db()) as db:
            with self.app.open_resource('schema.sql', mode='r') as f:
                db.cursor().executescript(f.read())
            db.commit()

    def connect_db(self):
        return sqlite3.connect(self.db_path)
