from database.tables.itable import ITable

class UsersResources (ITable):

    _tableName = "users_resources"

    def __init__(self, databaseName: str):
        self._databaseName = databaseName

    def up(self):
        return f"""
        CREATE TABLE IF NOT EXISTS {self._databaseName}.{self._tableName}
        (
             chat_id INT,
             resource_id INT,
             FOREIGN KEY(chat_id) REFERENCES users(chat_id),
             FOREIGN KEY(resource_id) REFERENCES resources(id)
        )"""

    def down(self):
        return f"""
        DROP TABLE {self._tableName}
        """

    @staticmethod
    def getTableName():
        return UsersResources._tableName

    def getName(self):
        return UsersResources._tableName