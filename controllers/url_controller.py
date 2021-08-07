from checks.user_check import UserCheck
from checks.datetime_cheker import CheckDateTime
from checks.url_cheker import CheckURL
from web_request.one_request import OneRequest
from database.requests.add_resource_to_user import AddResourceToUser
from views.resource_in_database import ResourceInDatabase


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
    def getAllURLs(update, context):
        pass

    @staticmethod
    def getAllURLsForThisUser(update, context):
        pass
