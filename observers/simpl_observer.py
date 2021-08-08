from observers.iobserver import IObserver
from timers.Itimer import ITimer
from controllers.url_controller import URLController
from web_request.one_request import OneRequest

class SimpObserver(IObserver):

    def __init__(self, timer: ITimer):
        self.timer(self)

    def checkResources(self):
        resources = URLController.getAllResources()
        for resource in resources:
            currentLastModified = OneRequest.getlastModified(resource.link)
            if not currentLastModified == resource.lastModified:
                pass
        # TODO
        # запросить все ресурсы из контроллера
        # для кажного ресурса получить его последние обновление
        # если обновление было,
        #   обновить данные в БД ( и сообщить пользывателям, которые подписаны на ресурс )
