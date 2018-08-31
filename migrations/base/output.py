from datetime import datetime
from colorama import Fore, Style
from enum import Enum


class OutputLevels(Enum):
    SUCCESS = Fore.GREEN
    WARNING = Fore.YELLOW
    ERROR = Fore.RED


class Output(object):
    message_default_success = '[{}] - [{}] Migrated Success!'
    message_default_error = '[{}] - [{}] Error on migration - {}'

    def __init__(self):
        self.__output_message = []

    def append_success(self, classname):
        timenow = str(datetime.now())
        self.__output_message.append(
            (OutputLevels.SUCCESS, Output.message_default_success.format(timenow, classname))
        )

    def append_error(self, classname, error):
        timenow = str(datetime.now())
        self.__output_message.append(
            (OutputLevels.ERROR, Output.message_default_error.format(timenow, classname, error))
        )

    def show(self):
        for level, message in self.__output_message:
            print(level.value + str(message))

        self.__output_message = []
