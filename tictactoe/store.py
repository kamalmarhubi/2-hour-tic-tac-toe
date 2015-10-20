import abc

class GameStore(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def put(self, key, game):
        pass

    @abc.abstractmethod
    def get(self, key):
        pass


class DictGameStore(GameStore):

    def __init__(self):
        self.games = dict()

    def put(self, key, game):
        self.games[key] = game

    def get(self, key):
        return self.games.get(key, None)
