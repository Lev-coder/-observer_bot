from database.Database import Database
from database.tables.Resources import Resurces
from database.modules.Resource import Resource

class GetResourceById:

    def __init__(self, urlId):
        self.urlId = urlId

    def start(self):
        database = Database()

        self.databaseName = database.getDatabaseName()
        self.cursor = database.getCursor()
        self.resurcesTableName = Resurces.getTableName()

        return self.GetResourceById()

    def GetResourceById(self):
        self.cursor.execute(self.sqlCommand())
        return self.cursor.fetchone()

    def sqlCommand(self):
        return f""" 
        SELECT * FROM {self.databaseName}.{self.resurcesTableName} 
            WHERE id = {self.urlId}
        """