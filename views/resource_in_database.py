
class ResourceInDatabase:
    def __init__(self,url, lastModified):
        self._url = url
        self._lastModified = lastModified

    def text(self):
        return f"""
the bot looks at the resource {self._url} - last-modified:{self._lastModified}
"""