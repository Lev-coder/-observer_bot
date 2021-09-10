from database.requests.AddUser import AddUser
from database.modules.Resource import Resource
from views.Menu import Menu
from app.services.checks.ExistCheker import ExistCheker
from app.services.checks.UserCheckr import UserCheck
from app.services.checks.ResourceCheck import ResourceCheck
from database.requests.GetUsersByResource import GetUsersByResource
from helpers.MessagesSender import MessagesSender


class UserController:

    @staticmethod
    def start(update, context):
        user = UserCheck.getUser(update)

        if not ExistCheker.isUserExist(user):
            AddUser(user).start()

        MessagesSender.sendMassage(update, Menu().text())

    @staticmethod
    def getUsersByResource(resource: Resource):
        if not ExistCheker.isURLExist(resource.link):
            raise Exception(f"resource not exist in database")

        users = GetUsersByResource(resource).start()
        for user in users:
            yield user