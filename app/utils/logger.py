import logging
from app.utils.config import Config

class Logger:
    __instance = None

    @staticmethod
    def GetLogger():
        """Static method to get the logger instance."""
        if Logger.__instance is None:
            Logger(log_file=Config.LOG_FILE_PATH)
        return Logger.__instance.logger

    def __init__(self, log_file=None):
        """Virtually private constructor."""
        if Logger.__instance is not None:
            raise Exception("Logger class is a singleton!")
        else:
            Logger.__instance = self
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.DEBUG)

            # create console handler and set level to debug
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_formatter = logging.Formatter('%(levelname)s: %(message)s')
            console_handler.setFormatter(console_formatter)
            self.logger.addHandler(console_handler)

            # create file handler and set level to info
            if log_file:
                file_handler = logging.FileHandler(log_file)
                file_handler.setLevel(logging.INFO)
                file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                file_handler.setFormatter(file_formatter)
                self.logger.addHandler(file_handler)

    def error(self, message, *args):
        self.logger.error(message, *args)

    def warning(self, message, *args):
        self.logger.warning(message, *args)

    def info(self, message, *args):
        self.logger.info(message, *args)
