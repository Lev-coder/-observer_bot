from database.database import Database
from database.requests.add_user import AddUser
from database.requests.add_resources import AddResources
from database.requests.get_resource import GetResource
from database.tables.users_resurces import UsersResources
from checks.user_check import UserCheck
from checks.url_cheker import CheckURL
from modules.resource import Resource

class AddResourceToUser:

    def __init__(self, chat_id, url, lastModified):
        self.chat_id = chat_id
        self.url = url
        self.lastModified = lastModified

    def start(self):
        database = Database()

        self.databaseName = database.getDatabaseName()
        self.cursor = database.getCursor()
        self.usersResourcesTableName = UsersResources.getTableName()

        if not UserCheck.isUserExist(self.chat_id):
            AddUser(self.chat_id).start()

        if not CheckURL.isURLExist(self.url):
            AddResources(self.url, self.lastModified).start()

        self.resource = Resource(GetResource(self.url).start())

        self.AddResourceToUser()

        database.saveChange()

    def AddResourceToUser(self):
        return self.cursor.execute(self.sqlCommand())

    def sqlCommand(self):
        return f""" 
        INSERT INTO {self.databaseName}.{self.usersResourcesTableName}(chat_id,resource_id) 
        VALUES ({self.chat_id},{self.resource.id})
        """