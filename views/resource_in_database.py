
class ResourceInDatabase:
    def __init__(self,url):
        self._url = url

    def text(self):
        return f"""
the bot looks at the resource {self._url}
"""