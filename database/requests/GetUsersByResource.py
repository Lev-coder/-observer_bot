from database.modules.Resource import Resource
from database.Database import Database
from database.tables.Users import Users
from database.requests.IRequests import IRequests
from database.tables.Resources import Resurces
from database.tables.UserResource import UsersResources
from database.modules.User import User

class GetUsersByResource(IRequests):

    def __init__(self, resourc: Resource):
        self._resourc = resourc

    def start(self):
        database = Database()

        self.cursor = database.getCursor()
        self.databaseName = database.getDatabaseName()
        self.userTable = Users.getTableName()
        self.resourceTable = Resurces.getTableName()
        self.usersResourcesTable = UsersResources.getTableName()

        for user_fields in self.GetUsersFieldsByResource():
            yield User(user_fields)

    def GetUsersFieldsByResource(self):
        self.cursor.execute(self.sqlCommand())
        return self.cursor.fetchall()


    def sqlCommand(self):
        return f""" 
        SELECT {self.databaseName}.{self.userTable}.chat_id FROM {self.databaseName}.{self.userTable} 
            JOIN {self.databaseName}.{self.usersResourcesTable} ON 
                {self.userTable}.chat_id = {self.usersResourcesTable}.chat_id
            JOIN {self.databaseName}.{self.resourceTable} ON
    	        {self.usersResourcesTable}.resource_id = {self.databaseName}.{self.resourceTable}.id 
    	    WHERE
                {self.resourceTable}.link = "{self._resourc.link}"
        """
