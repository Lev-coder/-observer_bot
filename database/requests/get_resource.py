from database.database import Database
from database.tables.resources import Resurces

class GetResource:

    def __init__(self, url):
        self.url = url

    def start(self):
        database = Database()

        self.databaseName = database.getDatabaseName()
        self.cursor = database.getCursor()
        self.resurcesTableName = Resurces.getTableName()

        return self.getResurces()

    def getResurces(self):
        self.cursor.execute(self.sqlCommand())
        return self.cursor.fetchone()

    def sqlCommand(self):
        return f""" 
        SELECT * FROM {self.databaseName}.{self.resurcesTableName} 
            WHERE link = {self.url}
        """