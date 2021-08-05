import sqlite3 as sqlite

from database.tables.itable import ITable
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
            if not table is ITable:
                raise ArithmeticError("table is not ITable")

            self._addTableToDatabase(table)
            self._createTable(self, cursor,table)


    def drop(self):
        cursor = self._connection.cursor()

        for table in Database._tables:
            Database._deleteTable(self, cursor, table)

    def getTable(self,table : ITable):
        if not table.getTableName() in self.tables:
            raise Exception("Database not have this table")
        return self.tables[ table.getTableName() ]

    def getCursor(self):
        return self._connection.cursor()

    def saveChange(self):
        self._connection.commit()
        return True

    def _deleteTable(self,cursor,table):
        try:
            cursor.execute(table.down())
        except Exception as error:
            print(f"error: {error}")
        print(f"delete table {table.getTableName()}")

    def _createTable(self,cursor,table):
        try:
            cursor.execute(table.up())
        except Exception as error:
            print(f"error: {error}")
        print(f"create table {table.getTableName()}")

    def _addTableToDatabase(self,table):
        self.tables[ table.getTableName() ] = table

    def __del__(self):
        self._connection.close()



