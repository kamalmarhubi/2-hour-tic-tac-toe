import abc

class GameStore(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def put(self, key, game):
        pass

    @abc.abstractmethod
    def get(self, key):
        pass
