from database.Database import Database
from database.requests.IRequests import IRequests
from database.tables.Users import Users
from database.tables.Resources import Resurces
from database.tables.UserResource import UsersResources
from database.modules.User import User
from database.modules.Resource import Resource

class isUserOwnerResource(IRequests):
    def __init__(self,user: User, resource: Resource):
        self._user = user
        self._resource = resource

    def start(self):
        database = Database()

        self.cursor = database.getCursor()
        self.databaseName = database.getDatabaseName()
        self.userTable = Users.getTableName()
        self.resourceTable = Resurces.getTableName()
        self.usersResourcesTable = UsersResources.getTableName()

        return self.isUserOwnerResource

    def isUserOwnerResource(self):
        self.cursor.execute(self.sqlCommand())
        return self.cursor.fetchone()

    def sqlCommand(self):
        return f""" 
        SELECT {self.databaseName}.{self.resourceTable}.{self._resource.id} FROM {self.databaseName}.{self.resourceTable} 
            JOIN {self.databaseName}.{self.usersResourcesTable} ON 
                {self.resourceTable}.{self._resource.id} = {self.usersResourcesTable}.{self._resource.id}
            JOIN {self.databaseName}.{self.userTable} ON
    	        {self.usersResourcesTable}.{self._user.chat_id} = {self.databaseName}.{self.userTable}.{self._user.chat_id} 
        """

