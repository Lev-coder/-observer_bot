import sqlite3 as sqlite

from tables import Resources
from tables import Users
from tables import UsersResurces

class Database:

    tables = [
        Resources,
        Users,
        UsersResurces,
    ]
    def __init__(self):
        for table in Database.tables:
            table.up()

    def stop(self):
        for table in Database.tables:
            table.down()


