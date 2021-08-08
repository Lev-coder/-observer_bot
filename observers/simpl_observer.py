from observers.iobserver import IObserver
from timers.Itimer import ITimer

class SimpObserver(IObserver):

    def __init__(self, timer: ITimer):
        self.timer(self)

    def checkResources(self):
        # TODO
        # запросить все ресурсы из контроллера
        # для кажного ресурса получить его последние обновление
        # если обновление было,
        #   обновить данные в БД ( и сообщить пользывателям, которые подписаны на ресурс )
        #

        pass