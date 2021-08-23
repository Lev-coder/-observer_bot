from database.Database import Database
from database.requests.AddUser import AddUser
from database.requests.AddResource import AddResource
from database.requests.GetResource import GetResource
from database.tables.UserResource import UsersResources
from app.services.checks.ExistCheker import ExistCheker
from database.modules.Resource import Resource
from database.modules.User import User

class AddResourceToUser:

    def __init__(self, user: User, url, lastModified):
        self._user = user
        self.url = url
        self.lastModified = lastModified

    def start(self):
        database = Database()

        self.databaseName = database.getDatabaseName()
        self.cursor = database.getCursor()
        self.usersResourcesTableName = UsersResources.getTableName()

        if not ExistCheker.isUserExist(self._user):
            AddUser(self._user).start()

        if not ExistCheker.isURLExist(self.url):
            AddResource(self.url, self.lastModified).start()

        self.resource = Resource(GetResource(self.url).start())

        self.AddResourceToUser()

        database.saveChange()

    def AddResourceToUser(self):
        return self.cursor.execute(self.sqlCommand())

    def sqlCommand(self):
        return f""" 
        INSERT INTO {self.databaseName}.{self.usersResourcesTableName}(chat_id,resource_id) 
        VALUES ({self._user.chat_id},{self.resource.id})
        """