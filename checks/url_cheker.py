import validators

class CheckURL:

    @staticmethod
    def isURLValide(url):
        return validators.url(url)

    @staticmethod
    def getURL(context):
        if len(context.args) == 0:
            raise Exception("give me URL (example:  /watch https://stepik.org/)")
        return context.args[0]