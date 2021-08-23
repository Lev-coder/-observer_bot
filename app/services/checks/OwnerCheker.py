from database.requests.isUserOwnerResource import isUserOwnerResource
from database.modules.User import User
from database.modules.Resource import Resource

class OwnerCheker:

    @staticmethod
    def isOwner(user: User,resource: Resource):
        return isUserOwnerResource(user,resource) != None