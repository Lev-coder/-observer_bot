from checks.url_cheker import CheckURL
from views.resource_in_database import ResourceInDatabase
from checks.user_check import UserCheck
from database.requests.add_resource_to_user import AddResourceToUser
from web_request.one_request import OneRequest

class URLController:

    @staticmethod
    def watch(update, context):

        url = CheckURL.getURL(context)
        chat_id = UserCheck.getChatId(update)
        lastModified = OneRequest(url).getlastModified()

        AddResourceToUser.start(chat_id, url, lastModified)

        update.message.reply_text(ResourceInDatabase(url).text())

    @staticmethod
    def getAllURLs():
        pass

    @staticmethod
    def getAllURLsForThisUser():
        pass
