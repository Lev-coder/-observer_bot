from database.database import Database

class FindUsersByResource:

    def __init__(self,link):
        self.link = link

    def start(self):
        self.cursor = Database.getCursor()
        self.userTable = Database.getTable("users")
        self.resourceTable = Database.getTable("resources")
        self.usersResourcesTable = Database.getTable("users_resources")

        self.findUsers(self.link)

    def findUsers(self):
        return self.cursor.execute(self.sqlCommand())

    def sqlCommand(self):
        return f""" 
        select chat_id from {self.userTable} 
            join {self.usersResourcesTable} on 
                {self.userTable}.chat_id = {self.usersResourcesTable}.chat_id
            join self.resourceTable on
                {self.usersResourcesTable}.resource_id = {self.resourceTable}.resource_id 
                and 
                {self.resourceTable}.link = {self.link}
        """
