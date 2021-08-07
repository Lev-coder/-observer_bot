from timers.Itimer import ITimer
from observers.simpl_observer import SimpObserver
import datetime

class IntervalTimer(ITimer):

    def __int__(self, interval, observer: SimpObserver):
        self.observer = observer
        self.startСountdown()

    def startСountdown(self):
        pass