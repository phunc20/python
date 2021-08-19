import logging
import sys

logging.basicConfig(filename="out.log", level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

logging.debug("stdout debug")
logging.info("stdout info")
logging.warning("stdout warning")
logging.error("stdout error")
