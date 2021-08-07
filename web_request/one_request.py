import requests

class OneRequest:

    def __init__(self, url: str):
        self.url = url
        self.webKey = "Last-Modified"

    def getlastModified(self):
        result = OneRequest.getRequests(self.url)
        if not self.webKey in result.headers:
            raise Exception(f"{self.webKey} not in response")

        return result.headers[self.webKey]

    @staticmethod
    def getRequests(url):
        try:
            return requests.get(url)
        except Exception as error:
            raise error