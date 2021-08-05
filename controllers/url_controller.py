from checks.url_cheker import CheckURL

class URLController:

    def watch(self,update, context):
        url = context(0)
        print(url)
        if not CheckURL.isURLValide(url):
            raise Exception("URL not valide")

        user = update.message.from_user
        chat_id = user['id']

        #записать этот ресур для этого чата
        #сообщить об удачном завершении работы
