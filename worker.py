__author__ = 'sergioska'

""" this class is a simple implementation of a worker 
    a demonizable object needs to extend the abstract Runnable class 
    and also it needs implement run method. """

import logging
from libs.runnable import Runnable

class Worker(Runnable):
    def __init__(self):
        logging.basicConfig(filename='example.log',level=logging.DEBUG)
        logging.debug('This message should go to the log file')
        logging.info('So should this')
        logging.warning('And this, too')
    def run(self):
        """ run method contains worker logic """
        logging.info("OK")
