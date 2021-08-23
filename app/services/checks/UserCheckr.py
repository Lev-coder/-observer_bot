from database.modules.User import User

class UserCheck:

    @staticmethod
    def getUser(update):
        user = update.message.from_user
        return User((user['id'],))
