from database.database import Database
from database.tables.users import Users

class GetUser:

    def __init__(self, chat_id):
        self.chat_id = chat_id

    def start(self):
        database = Database()

        self.databaseName = database.getDatabaseName()
        self.cursor = database.getCursor()
        self.userTableName = Users.getTableName()

        return self.getUser()

    def getUser(self):
        return self.cursor.execute(self.sqlCommand())

    def sqlCommand(self):
        return f""" 
        SELECT chat_id FROM {self.databaseName}.{self.userTableName} WHERE {self.chat_id}
        """