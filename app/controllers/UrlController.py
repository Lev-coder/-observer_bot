from app.services.checks.UserCheckr import UserCheck
from app.services.checks.DatetimeCheker import CheckDateTime
from app.services.checks.ResourceCheck import ResourceCheck
from app.services.checks.UrlIdCheker import UrlIdCheker
from app.services.checks.ExistCheker import ExistCheker
from app.services.checks.OwnerCheker import OwnerCheker
from helpers.MessagesSender import MessagesSender
from app.services.web_request.OneRequest import OneRequest
from database.requests.AddResourceToUser import AddResourceToUser
from database.requests.UpdateResource import UpdateResource
from database.requests.GetAllResources import GetAllResources
from database.requests.GetResourceById import GetResourceById
from database.requests.GetResource import GetResource
from database.requests.GetResourcesByUser import GetResourcesByUser
from database.requests.DeleteResource import DeleteResource
from views.ResourceInDatabase import ResourceInDatabase
from views.UserResources import UserResources
from views.errors.ResourceNotExist import ResourceNotExist
from views.errors.CommandWatchIncorrect import CommandWatchIncorrect
from database.modules.Resource import Resource

class URLController:

    @staticmethod
    def watch(update, context):

        messageIfFailured = lambda context: MessagesSender.sendMassage(update, CommandWatchIncorrect().text())
        url = ResourceCheck.getURLSafely(update, context, messageIfFailured) #TODO


        user = UserCheck.getUser(update)
        lastModified = CheckDateTime.getLastModified(
                            OneRequest(url).getlastModified()
                        )

        if not ExistCheker.isURLExist(url):
            AddResourceToUser(user, url, lastModified).start()

        resource = GetResource(url)
        if not OwnerCheker.isOwner(user,resource):
            AddResourceToUser(user,url,lastModified)

        massageText = ResourceInDatabase(url, lastModified).text()
        MessagesSender.sendMassage(update, massageText)

    @staticmethod
    def getAllURLsForThisUser(update, context):
        user = UserCheck.getUser(update)
        resources = GetResourcesByUser(user).start()
        MessagesSender.sendMassage(update, UserResources(resources).text())

    @staticmethod
    def deleteResource(update, context):
        urlId = UrlIdCheker.getUrlId(context)
        if not ExistCheker.isUrlIdExist(urlId):
            MessagesSender.sendMassage(update, ResourceNotExist(urlId).text())

        resource = Resource( GetResourceById(urlId).start() )
        user = UserCheck.getUser(update)
        if not OwnerCheker.isOwner(user,resource):
            MessagesSender.sendMassage(update, ResourceNotExist(urlId).text())

        DeleteResource(resource).start()

        resources = GetResourcesByUser(user).start()
        MessagesSender.sendMassage(update, UserResources(resources).text())

    @staticmethod
    def getAllResources():
        resources = GetAllResources().start()
        for resource in resources:
            yield Resource(resource)

    @staticmethod
    def updateResource(resource: Resource):
        if not ExistCheker.isURLExist(resource.link):
            raise Exception(f"URL {resource.link} not exist in database")
        UpdateResource(resource).start()



