from database.Database import Database
from database.modules.User import User
from database.modules.Resource import Resource
from database.tables.Users import Users
from database.tables.Resources import Resurces
from database.tables.UserResource import UsersResources
from database.requests.IRequests import IRequests

class GetResourcesByUser(IRequests):
    def __init__(self, user: User):
        self._user = user

    def start(self):
        database = Database()

        self.cursor = database.getCursor()
        self.databaseName = database.getDatabaseName()
        self.userTable = Users.getTableName()
        self.resourceTable = Resurces.getTableName()
        self.usersResourcesTable = UsersResources.getTableName()

        for resource_fields in self.getAllResourcesByUser():
            yield Resource(resource_fields)

    def getAllResourcesByUser(self):
        self.cursor.execute(self.sqlCommand())
        return self.cursor.fetchall()

    def sqlCommand(self):
        return f""" 
        SELECT  {self.databaseName}.{self.resourceTable}.id,
                {self.databaseName}.{self.resourceTable}.link,
                {self.databaseName}.{self.resourceTable}.last_modified
                
            FROM {self.databaseName}.{self.resourceTable} 
                JOIN {self.databaseName}.{self.usersResourcesTable} ON 
                    {self.resourceTable}.id = {self.usersResourcesTable}.resource_id
                JOIN {self.databaseName}.{self.userTable} ON
                    {self.databaseName}.{self.userTable}.chat_id = {self.usersResourcesTable}.chat_id
        """