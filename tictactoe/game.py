class Game(object):

    X = 'x'
    O = 'o'

    def __init__(self):
        self.turn = Game.X
        self.board = dict()
        
    def make_move(self, player, location):
        if player != self.turn:
            raise Exception('wrong player')

        if self.board.has_key(location):
            raise Exception('already played at %s' % location)

        self.board[location] = player
        self.turn = Game.O if self.turn == Game.X else Game.X

    def winner(self):
        """Returns Game.X, Game.O or None."""
        return None
