from datetime import timedelta
from config import TOKEN
from database.Database import Database
from loggers.ConsoleLoger import ConsoleLogger
from app.user_interface.bot.WatcherBot import WatcherBot
from app.services.observers.SimplObserver import SimpObserver
from app.services.timers.IntervalTimer import IntervalTimer
from helpers.DateTime import DateTime

if __name__ == '__main__':
    db = Database()
    bot = WatcherBot(TOKEN, ConsoleLogger)
    interval = DateTime(timedelta(seconds=10))
    observer = SimpObserver(
        bot,
        IntervalTimer(interval)
    )
    db.up()
    bot.start()