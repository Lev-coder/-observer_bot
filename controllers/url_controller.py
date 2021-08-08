from checks.user_check import UserCheck
from checks.datetime_cheker import CheckDateTime
from checks.url_cheker import CheckURL
from web_request.one_request import OneRequest
from database.requests.add_resource_to_user import AddResourceToUser
from database.requests.get_all_resources import GetAllResources
from views.resource_in_database import ResourceInDatabase
from modules.resource import Resource

class URLController:

    @staticmethod
    def watch(update, context):

        url = CheckURL.getURL(context)
        chat_id = UserCheck.getChatId(update)
        lastModified = CheckDateTime.getLastModified(
                        OneRequest(url).getlastModified()
                        )

        AddResourceToUser(chat_id, url, lastModified).start()

        update.message.reply_text(
            ResourceInDatabase(url,lastModified).text()
        )

    @staticmethod
    def getAllURLsForThisUser(update, context):
        pass

    @staticmethod
    def getAllResources():
        for resource in GetAllResources():
            yield Resource(resource)

    @staticmethod
    def updateResource(resource: Resource):
        if not CheckURL.isURLExist(resource.link):
            raise Exception(f"URL {resource.link} not exist in database")


