from observers.iobserver import IObserver

class SimpObserver(IObserver):

    def __init__(self, timer):
        self.timer(self)

    def checkResources(self):
        pass