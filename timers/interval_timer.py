from timers.Itimer import ITimer
from observers.simpl_observer import SimpObserver
from datetime import datetime
from multiprocessing import Process

class IntervalTimer(ITimer):

    def __int__(self, interval: datetime, observer: SimpObserver):
        self._interval = interval
        self._observer = observer

        Process(self.startСountdown).start()

    def startСountdown(self):
        initialInterval = datetime.now()
        while initialInterval < self._interval:
            currentDatetime = datetime.now()
            initialInterval = currentDatetime - initialInterval
        self._observer.checkResources()