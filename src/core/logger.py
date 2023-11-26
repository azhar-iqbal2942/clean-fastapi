import sys
from loguru import logger
from config.settings import env

format_string = (
    "<green>{time}</green> | <level>{level: <8}</level> | <level>{message}</level>"
)


def console_logger():
    logger.remove()

    logger.add(sys.stderr, format=format_string, level=env("LOG_LEVEL"))


def file_logger():
    logger.remove()
    logger.add(
        "app.log",
        rotation="1 week",
        format=format_string,
        level=env("LOG_LEVEL"),
    )


log_configurations = {"console": console_logger, "file": file_logger}


def setup_logger():
    log_type = env("LOG_TYPE", "console")
    log_configurations.get(log_type, file_logger)()


setup_logger()
