from datetime import datetime

class DateTime:

    def __init__(self, year=0,
                 month=0, day=0,
                 hour=0, minute=0,
                 second=0, microsecond=0):

        self._datetime = datetime(year, month, day, hour, minute, second, microsecond)

    def now(self):
        return DateTime(datetime.now())

    def getDateTime(self):
        return self._datetime

    def __lt__(self, other):
        return self.getDateTime() < other.getDateTime()

    def __gt__(self, other):
        return self.getDateTime() > other.getDateTime()

    def __sub__(self, other):
        difference = self.getDateTime() > other.getDateTime()
        return DateTime(difference)
