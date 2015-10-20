import abc
import pickle


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


class PickledDictGameStore(GameStore):

    def __init__(self, filename):
        self.filename = filename

        try:
            with open(self.filename) as f:
                self.games = pickle.load(f)
        except IOError as e:
            if e.errno != 2:  # 2 is ENOENT, ie file doesn't exist
                raise

            self.games = dict()
            with open(self.filename, 'w') as f:
                pickle.dump(self.games, f)

    def put(self, key, game):
        self.games[key] = game

        with open(self.filename, 'w') as f:
            pickle.dump(self.games, f)

    def get(self, key):
        return self.games.get(key, None)
