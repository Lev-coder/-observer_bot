from database.Database import Database
from database.tables.Resources import Resurces

class AddResource:

    def __init__(self, link, last_modified):
        self.link = link
        self.last_modified = last_modified

    def start(self):
        database = Database()

        self.databaseName = database.getDatabaseName()
        self.cursor = database.getCursor()
        self.resourceTable = Resurces.getTableName()

        self.addResource()

        database.saveChange()

    def addResource(self):
        return self.cursor.execute(self.sqlCommand())

    def sqlCommand(self):
        return f""" 
        INSERT INTO {self.databaseName}.{self.resourceTable}(link,last_modified) 
        VALUES ("{self.link}",'{self.last_modified}')
        """
