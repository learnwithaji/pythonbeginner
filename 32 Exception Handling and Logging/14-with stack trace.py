import logging

logging.basicConfig(filename='app.log', format=" %(asctime)s - %(message)s" )

try:
    result = 10 / 0
except ZeroDivisionError:
    logging.critical("Division by zero in critical operation!", exc_info=True)
