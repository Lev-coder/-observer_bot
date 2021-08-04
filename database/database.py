import sqlite3 as sqlite

from database.tables.resources import Resurces
from database.tables.users import Users
from database.tables.users_resurces import UsersResources

class Database:

    _tables = [
        Resurces(),
        Users(),
        UsersResources(),
    ]

    def __init__(self):
        for table in Database._tables:
            table.up()


    def stop(self):
        for table in Database.tables:
            table.down()


