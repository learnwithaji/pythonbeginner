import logging

logging.basicConfig(filename='app.log', level=logging.CRITICAL)

try:
    result = 10 / 0
except ZeroDivisionError:
    logging.critical("Division by zero in critical operation!")

