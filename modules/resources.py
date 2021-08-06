
class Resources:

    def __init__(self, id, link, lastModified):
        self.id = id
        self.link = link
        self.lastModified = lastModified

    def __int__(self, attribute_list):
        self.id = attribute_list[0]
        self.link = attribute_list[1]
        self.lastModified = attribute_list[2]