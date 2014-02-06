sympathy-for-the-daemon
=======================

Daemonize a worker object in python.
You can daemonize your object simply extending a worker object from Runnable class and implementing its run method.
```python
""" import daemon lib """
from libs.daemon import Daemon
""" include your worker class that it extends Runner class and implements run method """
from worker import Worker

if __name__ == "__main__":
    """ instance Worker object """
    worker = Worker()
    """ instance Daemon """
    daemon = Daemon()
    """ daemonize worker object """
    daemon.daemonize(worker)
```    

Worker extends Runnable and implment its run method. For example:  
```python
import logging
from libs.runnable import Runnable

class Worker(Runnable):
    def __init__(self):
        logging.basicConfig(filename='example.log',level=logging.DEBUG)
    
    """ ... """
    
    def run(self):
        """ run method contains worker logic """
        """ ... """
        """ write OK as debug line on example.log file
            one for second (default daemon loop is set to 1 sec)
            don't forget to kill the process!!!
        logging.info("OK")
        """ ... """
```

Main loop in Daemon class set an one second loop by default; you can change this loop time using setTime Daemon's method.

```python
""" 60 sec """
daemon.setTime(60)
```





