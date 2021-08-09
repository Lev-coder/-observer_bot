from database.database import Database

from config import TOKEN
from loggers.console_loger import ConsoleLogger
from bot.watcher_bot import WatcherBot

from observers.simpl_observer import SimpObserver
from timers.interval_timer import IntervalTimer

from timers.DateTime import DateTime

if __name__ == '__main__':

    db = Database()
    bot = WatcherBot(TOKEN, ConsoleLogger)
    a = DateTime()
    observer = SimpObserver(
        IntervalTimer(a),
        bot
    )

    db.up()
    bot.start()