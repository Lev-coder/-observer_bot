# import requests
# r =requests.get("https://hi-news.ru/wp-content/uploads/2021/08/java_development_x5_group-650x358.jpg")
#
# print(r.headers)
#
# print(r.headers['last-modified'])


from telegram.ext import Updater, CommandHandler

from database.database import Database

from config import TOKEN
from loggers.console_loger import ConsoleLogger
from controllers.url_controller import URLController
from controllers.user_controller import UserController

class Bot:

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

    def start(self):

        self._updater.start_polling()
        self._updater.idle()

        print("bot start")

if __name__ == '__main__':

    db = Database()
    bot = Bot(TOKEN, ConsoleLogger)

    db.up()
    bot.start()