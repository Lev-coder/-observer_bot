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

    _databaseName = "TheDatabase.db"

    def __init__(self):
        self._connection = sqlite.connect( Database._databaseName )
        cursor = self._connection.cursor()

        for table in Database._tables:
            Database._createTable(self, cursor,table)


    def stop(self):
        cursor = self._connection.cursor()

        for table in Database._tables:
            Database._deleteTable(self, cursor, table)


    def _deleteTable(self,cursor,table):
        try:
            cursor.execute(table.down())
        except Exception as error:
            print(error)
        print(f"delete table {table.getTableName()}")

    def _createTable(self,cursor,table):
        try:
            cursor.execute(table.up())
        except Exception as error:
            print(error)
        print(f"create table {table.getTableName()}")



