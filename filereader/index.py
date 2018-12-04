from logger.index import Logger
import time
import os

PATH = os.path.dirname(__file__)

class File:
    """File helper class to read and write to file"""

    __PATH = PATH + '/storage/'

    def __init__(self):
        self.logger = Logger()

    def read_file(self, path, file_name):
        """ Read from file """

        try:
            path = path + file_name
            with open(path, encoding='utf-8') as file:
                file_data = file.read()
            return file_data
        except FileNotFoundError as err:
            self.logger.log_message(err, self.logger.ERROR)

    def write_to_file(self, message, name):
        """Write to the file"""

        try:
            path = self.__PATH + name
            with open(path, 'w') as file:
                print(message, file=file)
        except FileNotFoundError as err:
            self.logger.log_message(err, self.logger.ERROR)

    def append_to_file(self, message, name):
        """Append to file."""

        try:
            path = self.__PATH + name
            with open(path, 'a') as file:
                print(message, file=file)
        except FileNotFoundError as err:
            self.logger.log_message(err, self.logger.ERROR)

    def list_all_files(self):
        """List all storage"""
        print("Files in the storage: ", os.listdir(self.__PATH))

    def read_file_timed(self, file_name):
        """Return the contents of the file at 'path' and measure time required."""

        start_time = time.time()

        self.read_file(self.__PATH, file_name)
        stop_time = time.time()
        time_difference = stop_time - start_time
        message = "Time required for reading {file} = {time}".format(file=file_name, time=time_difference)
        self.logger.log_message(message, self.logger.INFO)

    def write_to_file_timed(self, message, name):
        """Write to the file at 'path' and measure time required."""
        start_time = time.time()
        self.write_to_file(message, name)
        stop_time = time.time()
        time_difference = stop_time - start_time
        message = "Time required for writing to {file} = {time}".format(file=name, time=time_difference)
        self.logger.log_message(message, self.logger.INFO)

    def append_to_file_timed(self, message, name):
        """Write to the file at 'path' and measure time required."""

        start_time = time.time()

        stop_time = time.time()
        time_difference = stop_time - start_time
        message = "Time required for appending to {file} = {time}".format(file=name, time=time_difference)
        self.logger.log_message(message, self.logger.INFO)
