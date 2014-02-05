__author__ = 'sergioska'

'''
simple test script that show to daemonize a worker object
'''

from libs.daemon import Daemon
from worker import Worker

if __name__ == "__main__":
    worker = Worker()
    daemon = Daemon()
    daemon.daemonize(worker)

