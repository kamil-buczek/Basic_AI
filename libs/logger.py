# Std
import logging
import sys
from datetime import datetime

LOG_FILENAME = datetime.now().strftime('logs/logfile_%Y_%m_%d_%H_%M_%S.log')
FORMATTER = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')


def get_console_handler(debug_mode=False):
    consolehandler = logging.StreamHandler(sys.stdout)
    consolehandler.setFormatter(FORMATTER)
    if debug_mode:
        consolehandler.setLevel(logging.DEBUG)
    else:
        consolehandler.setLevel(logging.INFO)
    return consolehandler


def get_file_handler():
    filehandler = logging.FileHandler(LOG_FILENAME)
    filehandler.setLevel(logging.DEBUG)
    filehandler.setFormatter(FORMATTER)
    return filehandler


def set_console_handler_level(console_handler):
    console_handler.setLevel(logging.DEBUG)


def set_logger(logger_name, debug_mode=False):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)  # better to have too much log than not enough
    logger.addHandler(get_console_handler(debug_mode))
    logger.addHandler(get_file_handler())
    # with this pattern, it's rarely necessary to propagate the error up to parent
    logger.propagate = False
    return logger


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    return logger