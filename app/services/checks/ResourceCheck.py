import validators
from helpers.MessagesSender import MessagesSender

class ResourceCheck:

    @staticmethod
    def isURLValide(url):
        return validators.url(url)

    @staticmethod
    def getURL(context):

        if len(context.args) == 0:
            raise Exception("give me URL (example:  /watch https://stepik.org/)")

        url = context.args[0]

        if not ResourceCheck.isURLValide(url):
            raise Exception("URL not valide")

        return url

    @staticmethod
    def getURLSafely(update, context, callBackFunction):
        try:
            url = ResourceCheck.getURL(context)
            return url
        except:
            callBackFunction(update)