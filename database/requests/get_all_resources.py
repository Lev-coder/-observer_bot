from database.database import Database
from database.tables.resources import Resurces

class GetAllResources:

        def start(self):
            database = Database()

            self.databaseName = database.getDatabaseName()
            self.cursor = database.getCursor()
            self.resourceTable = Resurces.getTableName()

            self.getAllResources()

        def getAllResources(self):
            self.cursor.execute(self.sqlCommand())
            return self.cursor.fetchall()

        def sqlCommand(self):
            return f""" 
            SELECT * FROM {self.databaseName}.{self.resurcesTableName}"
            """
