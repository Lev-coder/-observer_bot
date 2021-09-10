from database.Database import Database
from database.modules.Resource import Resource
from database.tables.Resources import Resurces
from database.requests.IRequests import IRequests

class DeleteResource(IRequests):

    def __init__(self, resurces: Resource):
        self._resurces = resurces

    def start(self):
        database = Database()

        self.databaseName = database.getDatabaseName()
        self.cursor = database.getCursor()
        self.resourceTable = Resurces.getTableName()

        self.deleteResource()

        database.saveChange()

    def deleteResource(self):
        return self.cursor.execute(self.sqlCommand())

    def sqlCommand(self):
        return f""" 
        DELETE FROM  {self.databaseName}.{self.resourceTable} 
        WHERE {self.resourceTable}.id = {self._resurces.id}
        """