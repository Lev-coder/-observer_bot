from database.requests.get_user import GetUser

class UserCheck:

    @staticmethod
    def isUserExist(chat_id):
        #TODO напиши меня
        print(GetUser(chat_id).start())
        return True

    @staticmethod
    def getChatId(update):
        user = update.message.from_user
        return user['id']
