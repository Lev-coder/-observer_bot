from database.database import Database

class AddResources:

    def __init__(self,resource_id,link,last_modified):
        self.chat_id = resource_id
        self.link = link
        self.last_modified = last_modified

    def start(self):
        self.cursor = Database.getCursor()
        self.resourceTable = Database.getTable("resources")
        self.addResource(self.chat_id,self.link,self.last_modified)

    def addResource(self):
        return self.cursor.execute(self.sqlCommand())

    def sqlCommand(self):
        return f""" 
        INSERT INTO {self.userTable}(chat_id,link,last_modified) 
        VALUES({self.chat_id},{self.link},{self.last_modified})
        """
