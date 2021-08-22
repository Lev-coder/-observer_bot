from database.requests.GetUser import GetUser

class UserCheck:

    @staticmethod
    def isUserExist(chat_id):
        return GetUser(chat_id).start() != None

    @staticmethod
    def getChatId(update):
        user = update.message.from_user
        return user['id']
