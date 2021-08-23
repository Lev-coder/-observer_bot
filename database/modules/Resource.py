
class Resource:

    def __init__(self, attribute_list):
        self.id = attribute_list[0]
        self.link = attribute_list[1]
        self.lastModified = attribute_list[2]