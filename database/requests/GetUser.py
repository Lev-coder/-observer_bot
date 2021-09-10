from database.Database import Database
from database.tables.Users import Users
from database.requests.IRequests import IRequests

class GetUser(IRequests):

    def __init__(self, user: Users):
        self._user = user

    def start(self):
        database = Database()

        self.databaseName = database.getDatabaseName()
        self.cursor = database.getCursor()
        self.userTableName = Users.getTableName()

        return self.getUser()

    def getUser(self):
        self.cursor.execute(self.sqlCommand())
        return self.cursor.fetchone()

    def sqlCommand(self):
        return f""" 
        SELECT chat_id FROM {self.databaseName}.{self.userTableName} 
            WHERE chat_id = {self._user.chat_id}
        """