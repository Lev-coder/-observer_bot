from database.database import Database

class AddUser:

    def __init__(self,chat_id):
        self.chat_id = chat_id

    def start(self):
        self.cursor = Database.getCursor()
        self.userTable = Database.getTable("users")

        self.addUser(self.chat_id)

        Database.saveChange()

    def addUser(self):
        return self.cursor.execute(self.sqlCommand())

    def sqlCommand(self):
        return f""" 
        INSERT INTO {self.userTable}(chat_id) VALUES({self.chat_id})
        """
