import validators
from database.requests.get_resource import GetResource

class CheckURL:

    @staticmethod
    def isURLValide(url):
        return validators.url(url)

    @staticmethod
    def getURL(context):

        if len(context.args) == 0:
            raise Exception("give me URL (example:  /watch https://stepik.org/)")

        url = context.args[0]

        if not CheckURL.isURLValide(url):
            raise Exception("URL not valide")

        return url

    @staticmethod
    def isURLExist(url):
        return GetResource(url).start() != None
