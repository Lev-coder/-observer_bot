from database.requests.add_user import AddUser

class UserController:

    def addUser(self,update, context):
        user = update.message.from_user
        chat_id = user['id']

        AddUser().addUser(chat_id)

        #TODO отдать список команд (VIE)
