import logging.handlers
import datetime

logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler("all_logging.log",when="midnight",interval=1,backupCount=7,atTime=datetime.time(0,0,0,0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler("error.log")
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logger.debug("debug 信息")
logger.info("info 信息")
logger.warning("warning 信息")
logger.error("error 信息")
logger.critical("critical 信息")