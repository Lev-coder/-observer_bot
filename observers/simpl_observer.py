from observers.iobserver import IObserver
from timers.Itimer import ITimer
from controllers.url_controller import URLController
from controllers.user_controller import UserController
from web_request.one_request import OneRequest
from modules.resource import Resource
from modules.user import User
from sender.messages_sender import Sender
from views.have_chang import HaveChang

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


