from mysql.connector import connect, Error

from database.tables.itable import ITable
from database.tables.resources import Resurces
from database.tables.users import Users
from database.tables.users_resurces import UsersResources

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

        self._connection = connect(
            host = Database._host,
            user = Database._user,
            password = Database._password,
        )

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

    def getTable(self, table:str):
        if table.getTableName() not in self.tables:
            raise Exception("Database not have this table")
        return self.tables[table.getTableName()]

    def getCursor(self):
        return self._connection.cursor()

    def saveChange(self):
        self._connection.commit()
        return True

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
        print(f"create table {table.getTableName()}")

    def _deleteTable(self, cursor, table):
        try:
            cursor.execute(table.down())
        except Error as error:
            print(f"error: {error}")
        print(f"delete table {table.getTableName()}")

    def _addTableToDatabase(self, table):
        self.tables[table.getTableName()] = table

    def __del__(self):
        self._connection.close()
