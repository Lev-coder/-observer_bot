import validators

class CheckURL():

    def isURLValide(self, url):
        return validators.url(url)