import logging
from pathlib import Path
from datetime import datetime

class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    grey = "\x1b[38;10m"
    green = "\x1b[32;10m"
    turquoise = "\x1b[36;10m"
    yellow = "\x1b[33;10m"
    orange = "\x1b[31;5m"
    purple = "\x1b[35;10m"
    red = "\x1b[31;10m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format_ = "%(levelname)s - %(message)s (line:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: green + format_ + reset,
        logging.INFO: turquoise + format_ + reset,
        logging.WARNING: yellow + format_ + reset,
        logging.ERROR: orange + format_ + reset,
        logging.CRITICAL: bold_red + format_ + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


if __name__ == "__main__":
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    now = datetime.now().strftime("%Y%m%d-%H%M%S")
    log_path = Path(__file__).resolve().parent/f'{now}.log'
    logging.basicConfig(
        handlers=[
            logging.FileHandler(
                filename=log_path,
                encoding="utf8",
            )
        ],
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )
    logger = logging.getLogger()

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    #ch.setLevel(logging.DEBUG)
    ch.setFormatter(CustomFormatter())
    logger.setLevel(logging.DEBUG)
    logger.addHandler(ch)


    logger.debug("This is debug message.")
    logger.info("This is info message.")
    logger.warning("This is warning message.")
    logger.error("This is error message.")
    logger.critical("This is critical message.")
