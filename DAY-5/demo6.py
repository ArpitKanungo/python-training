import logging
logging.basicConfig(level=logging.INFO)

try:
    result = 10 / 0
except ZeroDivisionError as e:
    logging.error("An error occurred: %s", e)
finally:
    logging.info("Execution finished")