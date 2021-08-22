from database.modules.Resource import Resource

class HaveChang:

    def __init__(self, resource: Resource):
        self._resource = resource

    def text(self):
        return f"""
{self._resource.link} changed 
last-modified: {self._resource.lastModified}
    """