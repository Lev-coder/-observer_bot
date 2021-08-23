from database.tables.ITable import ITable

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
             
             PRIMARY KEY (chat_id, resource_id),
                 
             FOREIGN KEY(chat_id) REFERENCES users(chat_id) ON DELETE CASCADE,
             FOREIGN KEY(resource_id) REFERENCES resources(id) ON DELETE CASCADE
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