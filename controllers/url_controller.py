from checks.url_cheker import CheckURL
from views.resource_in_database import ResourceInDatabase
from checks.user_check import UserCheck
class URLController:

    @staticmethod
    def watch(update, context):

        url = CheckURL.getURL(context)

        if not CheckURL.isURLValide(url):
            raise Exception("URL not valide")

        chat_id = UserCheck.getChatId(update)


        #записать этот ресур для этого чата
        #сообщить об удачном завершении работы

        update.message.reply_text(ResourceInDatabase(url).text())
