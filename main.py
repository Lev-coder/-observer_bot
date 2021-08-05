from bs4 import BeautifulSoup
# import requests
# r =requests.get("https://hi-news.ru/wp-content/uploads/2021/08/java_development_x5_group-650x358.jpg")
#
# print(r.headers)
#
# print(r.headers['last-modified'])

from database.database import Database

# db = Database()
from telegram.ext import Updater, CommandHandler

from config import TOKEN
from loggers.console_loger import ConsoleLogger
from controllers.url_controller import URLController

class Bot:

    def __init__(self, token, iLoggerProvider):
        self._updater = Updater(TOKEN)
        self._dispatcher = self._updater.dispatcher
        self._logger = iLoggerProvider

        self.setHandlers()

    def setHandlers(self):
        self._dispatcher.add_handler(CommandHandler("watch", URLController.watch))

        self._dispatcher.add_error_handler(self._logger.error)

    def start(self):

        self._updater.start_polling()
        self._updater.idle()

        print("bot start")

if __name__ == '__main__':
    bot = Bot(TOKEN,ConsoleLogger)
    bot.start()
print("dfg")










