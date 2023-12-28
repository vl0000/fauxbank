import sqlite3

from os import environ

DB_NAME = environ.get('database', 'db.sqlite')

CONN = sqlite3.connect(DB_NAME)

CURSOR = CONN.cursor()



