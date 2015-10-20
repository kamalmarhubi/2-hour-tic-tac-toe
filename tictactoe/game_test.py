import unittest

from game import Game

class GameTest(unittest.TestCase):

    def test_make_move(self):
        game = Game()

        game.make_move(Game.X, (1, 1))

        with self.assertRaises(Exception):
            game.make_move(Game.X, (0, 0))

        with self.assertRaises(Exception):
            game.make_move(Game.O, (1, 1))

        game.make_move(Game.O, (0, 0))

        with self.assertRaises(Exception):
            game.make_move(Game.O, (2, 2))

        with self.assertRaises(Exception):
            game.make_move(Game.X, (0, 0))


if __name__ == '__main__':
    unittest.main()
