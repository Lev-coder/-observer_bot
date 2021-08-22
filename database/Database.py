from mysql.connector import connect, Error

from database.tables.ITable import ITable
from database.tables.Resources import Resurces
from database.tables.Users import Users
from database.tables.UserResource import UsersResources

class Database:

    _databaseName = "TheDatabase"
    _host = "localhost"
    _user = "root"
    _password = ""

    _tables = [
        Resurces,
        Users,
        UsersResources,
    ]

    def __init__(self):
        self.tables = {}
        self._connection = self.makeConnect()

    def up(self):
        cursor = self._connection.cursor()

        self._createDatabase(cursor)
        for table in Database._tables:
            # if  table is not ITable:
            #     raise ArithmeticError("table is not ITable")
            table = table(Database._databaseName)
            self._createTable(cursor, table)
            self._addTableToDatabase(table)

    def drop(self):
        cursor = self._connection.cursor()

        for table in Database._tables:
            table = table(Database._databaseName)
            Database._deleteTable(self, cursor, table(Database._databaseName))

    def getTable(self, tableName: str):
        if tableName not in self.tables:
            raise Exception("Database not have this table")
        return self.tables[tableName]

    def getCursor(self):
        return self._connection.cursor()

    def saveChange(self):
        self._connection.commit()
        return True

    def getDatabaseName(self):
        return Database._databaseName

    def _createDatabase(self,cursor):
        try:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Database._databaseName}")
        except Error as error:
            print(f"error: {error}")
        print(f"create database {Database._databaseName}")

    def _createTable(self, cursor, table):
        try:
            cursor.execute(table.up())
        except Error as error:
            print(f"error: {error}")
        print(f"create table {table.getName()}")

    def _deleteTable(self, cursor, table):
        try:
            cursor.execute(table.down())
        except Error as error:
            print(f"error: {error}")
        print(f"delete table {table.getName()}")

    def _addTableToDatabase(self, table):
        self.tables[table.getName()] = table

    def makeConnect(self):
        return connect(
            host=Database._host,
            user=Database._user,
            password=Database._password,
        )

    def __del__(self):
        self._connection.close()
