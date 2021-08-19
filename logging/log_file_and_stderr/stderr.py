import logging

logging.basicConfig(filename="err.log", level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())

logging.debug("This message should go to the log file")
logging.info("So should this")
logging.warning("And this, too")
logging.error("And non-ASCII stuff, too, like Øresund and Malmö")
