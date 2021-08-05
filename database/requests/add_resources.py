from database.database import Database

class AddResources:

    def __init__(self,link,last_modified):
        self.link = link
        self.last_modified = last_modified

    def start(self):
        self.cursor = Database.getCursor()
        self.resourceTable = Database.getTable("resources")

        self.addResource(self.link,self.last_modified)

        Database.saveChange()

    def addResource(self):
        return self.cursor.execute(self.sqlCommand())

    def sqlCommand(self):
        return f""" 
        INSERT INTO {self.userTable}(link,last_modified) 
        VALUES({self.link},{self.last_modified})
        """
