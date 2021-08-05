from database.requests.get_user import GetUser

class UserCheck:

    @staticmethod
    def isUserExist(chat_id):
        q = GetUser(chat_id).start()
        print(GetUser(chat_id).start())
        return True
