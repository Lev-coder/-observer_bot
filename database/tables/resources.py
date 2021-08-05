from database.tables.itable import ITable

class Resurces(ITable):

    _tableName = "resources"
    def __init__(self, databaseName: str):
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

    @staticmethod
    def getTableName():
        return Resurces._tableName

    def getName(self):
        return Resurces._tableName