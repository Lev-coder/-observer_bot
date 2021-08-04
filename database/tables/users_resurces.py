from database.tables.itable import ITable

class UsersResources (ITable):

    def __init__(self):
        self._tableName = "users_resources"

    def up(self):
        return f"""
        CREATE TABLE IF NOT EXISTS {self._tableName}
        (
             chat_id int,
             resource_id int
        )"""

    def down(self):
        return f"""
        DROP TABLE {self._tableName}
        """