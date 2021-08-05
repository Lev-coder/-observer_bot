from database.tables.itable import ITable

class Users(ITable):

    def __init__(self, databaseName: str):
        self._tableName = "users"
        self._databaseName = databaseName

    def up(self):
        return f"""
        CREATE TABLE IF NOT EXISTS {self._databaseName}.{self._tableName}
        (
             chat_id INT PRIMARY KEY
        )"""

    def down(self):
        return f"""
        DROP TABLE {self._tableName}
        """

    def getTableName(self):
        return self._tableName