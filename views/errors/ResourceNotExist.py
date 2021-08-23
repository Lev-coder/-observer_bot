
class ResourceNotExist:

    def __init__(self, urlId: int):
        self._urlId = urlId

    def text(self):
        return f"""
        resource numbered {self._urlId} 
        does not exist
        """