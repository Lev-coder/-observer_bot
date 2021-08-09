from telegram.ext import Updater, CommandHandler

from controllers.url_controller import URLController
from controllers.user_controller import UserController

class WatcherBot:

    def __init__(self, token, iLoggerProvider):
        self._updater = Updater(token)
        self._dispatcher = self._updater.dispatcher
        self._logger = iLoggerProvider

        self.setHandlers()

    def setHandlers(self):
        print("set handlers")

        self._dispatcher.add_handler(CommandHandler("start", UserController.start, pass_args=True))
        self._dispatcher.add_handler(CommandHandler("watch", URLController.watch, pass_args=True))

        self._dispatcher.add_error_handler(self._logger.error)

    def getUpdater(self):
        return  self._updater

    def start(self):
        print("bot start")

        self._updater.start_polling()
        self._updater.idle()