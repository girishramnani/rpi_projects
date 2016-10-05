__author__ = 'Girish'

import os

class CONFIG:
    ROOT =os.path.dirname(os.path.abspath(__file__))
    DATABASE = 'store.db'
    DEBUG = True
    SECRET_KEY = 'development key'
