from app.services.observers.IObserver import IObserver
from app.services.timers.ITimer import ITimer
from app.controllers.UrlController import URLController
from app.controllers.UserController import UserController
from app.services.web_request.OneRequest import OneRequest
from database.modules.Resource import Resource
from database.modules.User import User
from helpers.MessagesSender import Sender
from views.HaveChang import HaveChang

class SimpObserver(IObserver):

    def __init__(self, bot, timer: ITimer):
        self.bot = bot
        self.timer = timer

        timer.addSubscriber(self)

        timer.start()

    def checkResources(self):
        resources = URLController.getAllResources()
        for resource in resources:
            currentLastModified = OneRequest(resource.link).getlastModified()
            if not self._isResourceChanged(resource, currentLastModified):
                self._reportChange(resource)

    def _isResourceChanged(self, resource, currentLastModified):
        return resource.lastModified != currentLastModified

    def _reportChange(self, resource: Resource):
        for user in UserController.getUsersByResource(resource):
            self._sendMessage(user,resource)

        URLController.updateResource(resource)

    def _sendMessage(self,user: User,resource: Resource):
        massageText = HaveChang(resource).text()
        Sender.sendMassage(self.bot, user,massageText)


