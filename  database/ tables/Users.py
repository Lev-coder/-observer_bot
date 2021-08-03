import ITable

class Users(ITable):

    def __init__(self):
        self._tableName = "users"

    def up(self):
        return f"""
        CREATE TABLE IF NOT EXISTS {self._tableName}
        (
             chat_id int,
        )"""

    def down(self):
        return f"""
        DROP TABLE {self._tableName}
        """