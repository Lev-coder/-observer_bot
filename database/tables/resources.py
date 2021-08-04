from database.tables.itable import ITable

class Resurces (ITable):

    def __init__(self):
        self._tableName = "resources"

    def up(self):
        return f"""
        CREATE TABLE IF NOT EXISTS {self._tableName}
        (
             name text,
             link text
        )"""

    def down(self):
        return f"""
        DROP TABLE {self._tableName}
        """

    def getTableName(self):
        return self._tableName