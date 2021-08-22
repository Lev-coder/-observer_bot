from modules.resource import Resource
from database.database import Database
from database.tables.users import Users
from database.tables.resources import Resurces
from database.tables.users_resurces import UsersResources
from modules.user import User

class GetUsersByResource:

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
