from database.requests.GetUser import GetUser
from database.requests.GetResource import GetResource
from database.requests.GetResourceById import GetResourceById
from database.modules.User import User

class ExistCheker:
    @staticmethod
    def isURLExist(url):
        return GetResource(url).start() != None

    @staticmethod
    def isUrlIdExist(urlId):
        return GetResourceById(urlId).start() != None

    @staticmethod
    def isUserExist(user: User):
        return GetUser(user).start() != None