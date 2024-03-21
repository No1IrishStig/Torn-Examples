"""
Example Bot written by Stig [2648238]

This file contains some logging functions with custom colour formatting for each type of error

Use API Reference for more info:
https://docs.pycord.dev/en/stable/api/index.html
"""

import logging


class CustomFormatter(logging.Formatter):  # Custom Formatter to make logging nice and colourful
    green = '\033[92m'
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s: %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%d-%b-%y %H:%M:%S')
        return formatter.format(record)


def startLogging():
    # Create or retrieve logger
    logger = logging.getLogger("My_app")
    logger.setLevel(logging.DEBUG)  # Will capture all levels from DEBUG and above

    # Create file handler for saving logs to a file
    file_handler = logging.FileHandler(f'Utilities/bot.log', 'a')
    file_handler.setLevel(logging.DEBUG)  # Will capture all levels from DEBUG and above
    file_handler.setFormatter(logging.Formatter("%(asctime)s: [%(levelname)s] %(message)s", datefmt='%d-%b-%y %H:%M:%S'))
    logger.addHandler(file_handler)

    # Create console handler for printing logs to console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # Will capture all levels from INFO and above
    console_handler.setFormatter(CustomFormatter())
    logger.addHandler(console_handler)

    return logger
