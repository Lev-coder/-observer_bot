from telegram.ext import Updater, CommandHandler

from app.controllers.UrlController import URLController
from app.controllers.UserController import UserController

class WatcherBot:

    def __init__(self, token, iLoggerProvider):
        self._updater = Updater(token)
        self._bot = self._updater.bot
        self._dispatcher = self._updater.dispatcher
        self._logger = iLoggerProvider

        self.setHandlers()

    def setHandlers(self):
        print("set handlers")

        self._dispatcher.add_handler(CommandHandler("start", UserController.start, pass_args=True))
        self._dispatcher.add_handler(CommandHandler("watch", URLController.watch, pass_args=True))
        self._dispatcher.add_handler(CommandHandler("all", URLController.getAllURLsForThisUser, pass_args=True))
        self._dispatcher.add_handler(CommandHandler("del", URLController.deleteResource, pass_args=True))

        self._dispatcher.add_error_handler(self._logger.error)

    def getUpdater(self):
        return  self._updater

    def sendMessage(self,user,massageText: str):
        self._bot.send_message(user.chat_id,massageText)

    def start(self):
        print("bot start")

        self._updater.start_polling()
        self._updater.idle()