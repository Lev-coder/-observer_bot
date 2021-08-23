
class UrlIdCheker():

    @staticmethod
    def getUrlId(context):
        if len(context.args) == 0:
            raise Exception("give me url_number (example:  /del 343")

        urlNumber = context.args[0]

        return urlNumber