import logging

logging.basicConfig(filename='app.log', level=logging.INFO, format='[%(asctime)s] [%(levelname)s] [%(message)s]')

logging.info("Script started.")
logging.warning("Low disk space.")
logging.error("Database connection failed.")