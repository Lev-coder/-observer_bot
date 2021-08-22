from dateutil.parser import parse

class CheckDateTime:

    @staticmethod
    def getLastModified(lastModified: str):
        dateFormPrse = parse(lastModified)
        dateWithoutTimeZone = str(dateFormPrse).split("+")[0]
        return dateWithoutTimeZone