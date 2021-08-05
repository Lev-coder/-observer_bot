from checks.url_cheker import CheckURL
from views.resource_in_database import ResourceInDatabase
class URLController:

    @staticmethod
    def watch(update, context):
        url = context(0)
        print(url)
        if not CheckURL.isURLValide(url):
            raise Exception("URL not valide")

        user = update.message.from_user
        chat_id = user['id']

        #записать этот ресур для этого чата
        #сообщить об удачном завершении работы

        update.message.reply_text(ResourceInDatabase(url).text())
