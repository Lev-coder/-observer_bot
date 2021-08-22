from app.services.checks.UserCheckr import UserCheck
from app.services.checks.DatetimeCheker import CheckDateTime
from app.services.checks.UrlCheker import CheckURL
from helpers.MessagesSender import Sender
from app.services.web_request.OneRequest import OneRequest
from database.requests.AddResourceToUser import AddResourceToUser
from database.requests.UpdateResource import UpdateResource
from database.requests.GetAllResources import GetAllResources
from views.ResourceInDatabase import ResourceInDatabase
from database.modules.Resource import Resource

class URLController:

    @staticmethod
    def watch(update, context):

        url = CheckURL.getURL(context)
        chat_id = UserCheck.getChatId(update)
        lastModified = CheckDateTime.getLastModified(
                        OneRequest(url).getlastModified()
                        )

        AddResourceToUser(chat_id, url, lastModified).start()

        massageText = ResourceInDatabase(url,lastModified).text()
        Sender.sendMassage(update, massageText)


    @staticmethod
    def getAllURLsForThisUser(update, context):
        pass

    @staticmethod
    def getAllResources():
        resources = GetAllResources().start()
        for resource in resources:
            yield Resource(resource)

    @staticmethod
    def updateResource(resource: Resource):
        if not CheckURL.isURLExist(resource.link):
            raise Exception(f"URL {resource.link} not exist in database")
        UpdateResource(resource).start()



