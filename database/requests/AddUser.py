from database.Database import Database
from database.modules.User import User
from database.tables.Users import Users

class AddUser:

    def __init__(self,user: User):
        self._user = user

    def start(self):
        database = Database()

        self.databaseName = database.getDatabaseName()
        self.cursor = database.getCursor()
        self.userTableName = Users.getTableName()

        self.addUser()

        database.saveChange()

    def addUser(self):
        return self.cursor.execute(self.sqlCommand())

    def sqlCommand(self):
        return f""" 
        INSERT INTO {self.databaseName}.{self.userTableName}(chat_id) 
        VALUES ({self._user.chat_id})
        """
