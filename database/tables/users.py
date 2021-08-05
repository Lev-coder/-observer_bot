from database.tables.itable import ITable

class Users(ITable):

    _tableName = "users"

    def __init__(self, databaseName: str):
        self._databaseName = databaseName

    def up(self):
        return f"""
        CREATE TABLE IF NOT EXISTS {self._databaseName}.{self._tableName}
        (
             chat_id INT PRIMARY KEY
        )"""

    def down(self):
        return f"""
        DROP TABLE {self._databaseName}.{self._tableName}
        """

    @staticmethod
    def getTableName():
        return Users._tableName

    def getName(self):
        return Users._tableName