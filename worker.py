__author__ = 'sergioska'

import logging
from libs.runnable import Runnable

class Worker(Runnable):
    def __init__(self):
        logging.basicConfig(filename='example.log',level=logging.DEBUG)
        logging.debug('This message should go to the log file')
        logging.info('So should this')
        logging.warning('And this, too')
    def run(self):
        logging.info("OK")
