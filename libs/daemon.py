__author__ = 'sergioska'

import os
import time

class Daemon:

    def __init__(self):
        self.WORKINGDIR = "/"
        self.UMASK = 0
        self.sleepTime = 1

    def daemonize(self, worker):
        try:
            # fork a process from parent processor so father can exit and return control to the shell
            pid = os.fork()
        except OSError, e:
            raise Exception, "%s [%d]" % (e.strerror, e.errno)
        if (pid == 0):
            # set child process as session leader
            os.setsid()
            try:
                # fork another child to avoid zombies
                os.fork()
            except OSError, e:
                raise Exception, "%s [%d]" % (e.strerror, e.errno)
            if (pid == 0):
                os.chdir(self.WORKINGDIR)
                os.umask(self.UMASK)
                while True:
                    worker.run()
                    time.sleep(self.sleepTime)
            else:
                os._exit(0)
        else:
            os._exit(0)
        os.dup2(0, 1)
        os.dup2(0, 2)
        return(0)

    def setTime(self, nTime):
        self.sleepTime = nTime

