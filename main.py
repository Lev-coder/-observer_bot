# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from bs4 import BeautifulSoup
# import requests
# r = requests.get("https://hi-news.ru/wp-content/uploads/2021/08/java_development_x5_group-650x358.jpg")
#
# print(r.headers)
#
# print(r.headers['last-modified'])

from database.database import Database

# db = Database()
from telegram.ext import Updater, CommandHandler

from Logger.console_loger import ConsoleLogger
from config import TOKEN

class Bot:

    def __init__(self, token, iLoggerProvider):
        self._updater = Updater(TOKEN)
        self._dispatcher = self._updater.dispatcher
        self._logger = iLoggerProvider

        self.setHandlers()

    def setHandlers(self):
        self._dispatcher.add_handler(CommandHandler("start", lambda : print("he")))

        self._dispatcher.add_error_handler(self._logger.error)

    def start(self):
        self._updater.start_polling()
        self._updater.idle()

if __name__ == '__main__':
    bot = Bot(TOKEN,ConsoleLogger)
    bot.start()










