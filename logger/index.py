import logging
import os
# https://docs.python.org/3/howto/logging-cookbook.html

ABSOLUTE_PATH = os.path.abspath(os.path.dirname(__file__))


class Logger:
    """
    Helper class logger for logging
    @return: get_logger - return logger
    @functions: debug, info, error, warning, critical
    Use: logger = Logger()
         logger.log_message("Text123", "debug")
    """

    LOG_FORMAT = "%(levelname)s: %(asctime)s - %(message)s"
    FILE_NAME = ABSOLUTE_PATH + '/logs/logs.txt'
    LEVEL = logging.DEBUG
    TYPES = ['notset', 'debug', 'info', 'warning', 'error', 'critical']
    DEBUG = 'debug'
    INFO = 'info'
    WARNING = 'warning'
    ERROR = 'error'
    CRITICAL = 'critical'
    RED = '\33[31m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    CEND = '\33[0m'

    def __init__(self):
        """Create an logger basic config to overwrite file add filemode='w'"""
        logging.basicConfig(filename=self.FILE_NAME, level=self.LEVEL, format=self.LOG_FORMAT)
        self.logger = logging.getLogger()

    def __getitem__(self, name):
        return getattr(self, name)

    def print_logger_level(self):
        """
        Print logger level:
        Levels: Debug(10), Info(20), Warning(30), Error(40), Critical(50)
        """
        logger_instance = self.logger
        print(logger_instance.level)

    def log_message(self, message, level=INFO):
        """Log message to logs/logs.txt file
           self.TYPES.index(level) * 10 index is from 0 - 5 * 10
           get the level in integer
         """

        if level not in self.TYPES:
            print("Need to add correct level [debug, info, warning, error, critical]")
            return

        level_type = self.TYPES.index(level) * 10
        logger_instance = self.logger
        logger_instance.log(level_type, message)

    def print_logs(self):
        """Print all from logs.txt file:"""
        try:
            with open(self.FILE_NAME) as file:
                file_data = file.read()
            self.colored(file_data)
        except FileNotFoundError as err:
            self.logger.log_message(err, self.logger.ERROR)

    def colored(self, data):
        """Output data to console in colors"""
        log_list = data.split('\n')
        for message in log_list:
            if message.startswith('INFO'):
                print(self.BLUE + message + self.CEND)

            if message.startswith('WARNING'):
                print(self.YELLOW + message + self.CEND)

            if message.startswith('ERROR') or message.startswith('CRITICAL'):
                print(self.RED + message + self.CEND)

    def print_in_color(self, message, color):
        """Output data to console in colors: 'RED', 'YELLOW', 'BLUE'"""
        colors = ['RED', 'YELLOW', 'BLUE']
        color = color.upper()
        if color in colors:
            print(self[color] + message + self.CEND)
            return

        print(message)

