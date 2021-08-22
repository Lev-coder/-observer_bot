from database.requests.add_user import AddUser
from modules.resource import Resource
from modules.user import User
from views.menu import Menu
from checks.user_check import UserCheck
from checks.url_cheker import CheckURL
from database.requests.get_users_by_resource import GetUsersByResource
from sender.messages_sender import Sender

class UserController:

    @staticmethod
    def start(update, context):
        chat_id = UserCheck.getChatId(update)

        if not UserCheck.isUserExist(chat_id):
            AddUser(chat_id).start()

        Sender.sendMassage(update, Menu().text())

    @staticmethod
    def getUsersByResource(resource: Resource):
        if not CheckURL.isURLExist(resource.link):
            raise Exception(f"resource not exist in database")

        users = GetUsersByResource(resource).start()
        for user in users:
            yield user

