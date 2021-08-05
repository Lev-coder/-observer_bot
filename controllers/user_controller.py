from database.requests.add_user import AddUser
from views.menu import Menu
from checks.user_check import UserCheck

class UserController:

    @staticmethod
    def start(update, context):

        user = update.message.from_user
        chat_id = user.id

        if not UserCheck.isUserExist(chat_id):
            AddUser(chat_id).start()

        update.message.reply_text( Menu().text() )
