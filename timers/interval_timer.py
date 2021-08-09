from timers.Itimer import ITimer
from observers.iobserver import IObserver
from timers.DateTime import DateTime
from multiprocessing import Process

class IntervalTimer(ITimer):

    def __init__(self, interval: DateTime):
        self._interval = interval
        self._subscribes = []

        Process(self.startСountdown).start()

    def startСountdown(self):
        initialInterval = DateTime.now()
        while initialInterval < self._interval:
            currentDatetime = DateTime.now()
            initialInterval = currentDatetime - initialInterval

        self._infoSubscribers()

    def addSubscriber(self, subscriber: IObserver):
        self._subscribes.append(subscriber)

    def _infoSubscribers(self):
        for subscribe in self._subscribes:
            subscribe.checkResources()