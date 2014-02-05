__author__ = 'sergioska'

import abc

class Runnable(object):
    """ Runnable is an abstract class that daemonized object needs to implement """
    
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def run(self):
        raise NotImplementedError( "Should have implemented this" )


