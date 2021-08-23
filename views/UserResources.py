
class UserResources:
    def __init__(self, resources):
        self._resources = resources

    def text(self):
        if self._resources == None:
            return "you have no resources"

        map_function = lambda resource: f"{resource.id} {resource.link}"
        lines = map(map_function,self._resources)
        return "\n".join(lines)