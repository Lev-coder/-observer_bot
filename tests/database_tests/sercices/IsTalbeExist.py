from database.requests.IRequests import IRequests
from database.Database import Database

class IsTableExist(IRequests):

    def __init__(self,tableName,databaseName="thedatabase"):
        self._tableName = tableName
        self._databaseName = databaseName

    def start(self):
        database = Database()

        self._cursor = database.getCursor()

        return self._IsTableExist()

    def _IsTableExist(self):
        return self._IsTableExistRequests()[0] != None

    def _IsTableExistRequests(self):
        self._cursor.execute(self._sqlCommand())
        return self._cursor.fetchone()

    def _sqlCommand(self):
        return f""" 
            SELECT * FROM information_schema.tables
            WHERE table_schema = "{self._databaseName}" and 
                table_name = "{self._tableName}"
        """

    def __del__(self):
        self._cursor.close()

