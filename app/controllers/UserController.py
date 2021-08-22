from database.requests.AddUser import AddUser
from database.modules.Resource import Resource
from views.Menu import Menu
from app.services.checks.UserCheckr import UserCheck
from app.services.checks.UrlCheker import CheckURL
from database.requests.GetUsersByResource import GetUsersByResource
from helpers.MessagesSender import Sender

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

