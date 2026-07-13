import logging

# Basic setup
logging.basicConfig(filename='app.log', level=logging.INFO, format='[%(asctime)s] - %(levelname)s - %(message)s')
logging.info("information")

# Exception logging
try:
	number = 4 / 0
except ZeroDivisionError:
	logging.exception("Division failed")


## Advanced logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('app.log')
logger.addHandler(file_handler)
formatter = logging.Formatter('[%(asctime)s] - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.info("Advanced logging information")
