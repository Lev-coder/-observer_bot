import logging
from loggers.ilogger import ILogger
class ConsoleLogger(ILogger):

    def __init__(self):
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        self._logger = logging.getLogger(__name__)

    def error(self, update, context):
        # self._logger.warning('Update "%s" caused error "%s"', update, context.error)
        print("error")