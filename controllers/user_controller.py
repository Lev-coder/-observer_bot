
class UserController:

    def addUser(self,update, context):
        user = update.message.from_user
        chat_id = user['id']
