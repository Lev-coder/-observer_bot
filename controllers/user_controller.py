from database.requests.add_user import AddUser
from views.menu import Menu
class UserController:

    @staticmethod
    def start(update, context):
        user = update.message.from_user
        chat_id = user.id

        AddUser(chat_id).start()

        update.message.reply_text( Menu().text() )
