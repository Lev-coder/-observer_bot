from database.tables.itable import ITable

class Resurces (ITable):

    def __init__(self, databaseName: str):
        self._tableName = "resources"
        self._databaseName = databaseName

    def up(self):
        return f"""
        CREATE TABLE IF NOT EXISTS {self._databaseName}.{self._tableName}
        (
             id INT AUTO_INCREMENT PRIMARY KEY,
             link text,
             last_modified timestamp
        )"""

    def down(self):
        return f"""
        DROP TABLE {self._tableName}
        """

    def getTableName(self):
        return self._tableName