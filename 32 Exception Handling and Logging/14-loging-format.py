import logging

logging.basicConfig(filename='app.log', format="%(asctime)s - %(pathname)s - %(lineno)d - %(message)s" )

try:
    result = 10 / 0
except ZeroDivisionError:
    logging.critical("Division by zero in critical operation!")
