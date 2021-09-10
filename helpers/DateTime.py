from datetime import datetime, timedelta

class DateTime():

    def __init__(self,theDatetime: timedelta):
        self.theDatetime = theDatetime
        self.restart()

    @staticmethod
    def now():
        strTime = datetime.now()
        return DateTime._translateIntoTime(strTime)

    def getDateTime(self):
        return self._datetime

    def restart(self):
        nowDatetime = DateTime.now()
        self._datetime = self.theDatetime + nowDatetime

    def __lt__(self, other):
        return self.getDateTime() < other

    def __gt__(self, other):
        return self.getDateTime() > other

    def __sub__(self, other):
        difference = self.getDateTime() - other
        return DateTime(difference)

    def __add__(self, other):
        sum = self.getDateTime() + other.getDateTime()
        return DateTime(sum)

    @staticmethod
    def _translateIntoTime( strTime: str):
        if type(strTime) is datetime:
            return strTime
        return datetime.strptime(strTime, '%Y-%m-%d %H:%M:%S')