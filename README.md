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


