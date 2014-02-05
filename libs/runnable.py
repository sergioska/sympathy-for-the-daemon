__author__ = 'sergioska'

import abc

class Runnable(object):
    """ Runnable is an abstract class that daemonized object needs to implement """
    
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def run(self):
        """ this method is called in loop daemon """
        raise NotImplementedError( "Should have implemented this" )


