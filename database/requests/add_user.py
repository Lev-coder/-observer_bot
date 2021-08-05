from database.database import Database
from database.tables.users import Users
class AddUser:

    def __init__(self,chat_id):
        self.chat_id = chat_id

    def start(self):
        database = Database()

        self.databaseName = database.getDatabaseName()
        self.cursor = database.getCursor()
        self.userTableName = Users("s").getTableName()

        self.addUser()

        database.saveChange()

    def addUser(self):
        return self.cursor.execute(self.sqlCommand())

    def sqlCommand(self):
        return f""" 

        INSERT INTO {self.databaseName}.{self.userTableName}(chat_id) VALUES ({self.chat_id})
        """
