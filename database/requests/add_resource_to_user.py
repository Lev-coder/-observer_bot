from database.database import Database
from database.requests.add_user import AddUser
from database.requests.add_resources import AddResources
from database.requests.get_resource import GetResource
from database.tables.users_resurces import UsersResources
from checks.user_check import UserCheck
from checks.url_cheker import CheckURL
from modules.resources import Resources

class AddResourceToUser:

    def __init__(self, chat_id, link, lastModified):
        self.chat_id = chat_id
        self.link = link
        self.lastModified = lastModified

    def start(self):
        database = Database()

        self.databaseName = database.getDatabaseName()
        self.cursor = database.getCursor()
        self.usersResourcesTableName = UsersResources.getTableName()

        if not UserCheck.isUserExist(self.chat_id):
            AddUser(self.chat_id)

        if not CheckURL.isURLExist(self.url):
            AddResources(self.link, self.lastModified)

        self.resource = Resources(GetResource(self.url))

        self.AddResourceToUser()

        Database.saveChange()

    def AddResourceToUser(self):
        return self.cursor.execute(self.sqlCommand())

    def sqlCommand(self):
        return f""" 
        INSERT INTO {self.databaseName}.{self.usersResourcesTableName}(chat_id,resource_id) 
        VALUES ({self.chat_id},{self.resource.id})
        """