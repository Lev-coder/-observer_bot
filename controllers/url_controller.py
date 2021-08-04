from checks.url_cheker import CheckURL

class URLController:

    def watch(self,update, context):
        url = context(0)
        if not CheckURL.isURLValide(url):
            #TODO пинуть исключение
        #записать этот ресур для этого чата
        #сообщить об удачном завершении работы
