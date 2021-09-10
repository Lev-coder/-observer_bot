from database.Database import Database
from database.tables.Resources import Resurces
from database.requests.IRequests import IRequests

class GetAllResources(IRequests):

        def start(self):
            database = Database()

            self.databaseName = database.getDatabaseName()
            self.cursor = database.getCursor()
            self.resurcesTableName = Resurces.getTableName()

            return self.getAllResources()

        def getAllResources(self):
            self.cursor.execute(self.sqlCommand())
            return self.cursor.fetchall()

        def sqlCommand(self):
            return f""" 
            SELECT * FROM {self.databaseName}.{self.resurcesTableName}
            """
