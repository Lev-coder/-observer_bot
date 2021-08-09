from database.database import Database
from modules.resource import Resource
from database.database import Database
from database.tables.users import Users
from database.tables.resources import Resurces
from database.tables.users_resurces import UsersResources

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

        self.getUsersByResource()

    def getUsersByResource(self):
        self.cursor.execute(self.sqlCommand())
        return self.cursor.fetchall()

    def sqlCommand(self):
        return f""" 
        SELECT chat_id FROM {self.databaseName}.{self.userTable} 
            JOIN {self.usersResourcesTable} ON 
                {self.userTable}.chat_id = {self.usersResourcesTable}.chat_id
            JOIN {self.resourceTable} ON
                {self.usersResourcesTable}.resource_id = {self.resourceTable}.resource_id 
                AND 
                {self.resourceTable}.link = {self._resourc.link}
        """
