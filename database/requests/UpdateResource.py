from database.modules.Resource import Resource
from database.Database import Database
from database.tables.Resources import Resurces

class UpdateResource:
    def __init__(self, resource: Resource):
        self._resource = resource

    def start(self):
        database = Database()

        self.databaseName = database.getDatabaseName()
        self.cursor = database.getCursor()
        self.resurcesTableName = Resurces.getTableName()

        self.updateResource()

        database.saveChange()

    def updateResource(self):
        return self.cursor.execute(self.sqlCommand())
    # TODO
    def sqlCommand(self):
        return f""" 
        UPDATE {self.databaseName}.{self.resurcesTableName} 
            SET  {self.resurcesTableName}.last_modified = "{self._resource.lastModified}"
            WHERE {self.resurcesTableName}.id = {self._resource.id}
        """