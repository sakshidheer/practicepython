import logging
import sys
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

def log_piramid(lines):
    to_print = ""
    for index in range(lines):
        for space in range(lines-(index+1)):
           to_print = to_print+ ' '
        for astrick in range((index*2)+1):
           to_print = to_print + '*'
        logging.info(to_print)
        to_print = ""

log_piramid(7)