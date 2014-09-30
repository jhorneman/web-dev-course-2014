import unittest
from models import GameState


class GameStateModelTestCase(unittest.TestCase):
    def test_creation(self):
    	gs = GameState()

    def test_row_wins(self):
    	gs = GameState.create_from_string("xxxoo o  ")
    	assert gs.state == GameState.Player1Won

    def test_vertical_row_wins(self):
    	gs = GameState.create_from_string("xo x oxo  ")
    	assert gs.state == GameState.Player1Won

    def test_diagonals_win(self):
    	gs = GameState.create_from_string("xo ox o x")
    	assert gs.state == GameState.Player1Won
    	gs = GameState.create_from_string(" oxox x o")
    	assert gs.state == GameState.Player1Won

    def test_draw(self):
    	gs = GameState.create_from_string("oxoxxoxox")
    	assert gs.state == GameState.Draw

    def test_ongoing(self):
    	gs = GameState.create_from_string("oxoxxoxo ")
    	assert gs.state == GameState.Ongoing


if __name__ == '__main__':
    unittest.main()
