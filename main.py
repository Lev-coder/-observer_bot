from database.database import Database

from config import TOKEN
from loggers.console_loger import ConsoleLogger
from bot.watcher_bot import WatcherBot

from observers.simpl_observer import SimpObserver
from timers.interval_timer import IntervalTimer

from timers.re_date_time.DateTime import DateTime
from datetime import timedelta

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