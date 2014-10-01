import unittest
from models import GameState
from application import create_app


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

    def test_make_move(self):
    	gs = GameState()
    	gs.make_move(0, 0)
    	assert gs.state == GameState.Ongoing

    def test_make_move_updates_state(self):
    	gs = GameState.create_from_string(" xoxxoxox")
    	gs.make_move(0, 0)
    	assert gs.state == GameState.Player1Won

    def test_make_move_asserts(self):
    	gs = GameState()
    	self.assertRaises(AssertionError, gs.make_move, -1, 0)
    	self.assertRaises(AssertionError, gs.make_move, 0, 3)

    	gs = GameState.create_from_string("oxoxxoxox")
    	self.assertRaises(AssertionError, gs.make_move, 0, 0)

    	gs = GameState.create_from_string(" xoxxoxox")
    	self.assertRaises(AssertionError, gs.make_move, 2, 2)


app = create_app()
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['TESTING'] = True
# app.config['WTF_CSRF_ENABLED'] = False


class WebTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.gs = app.gs

    def test_index_page(self):
        rv = self.client.get('/')
        assert "Tic Tac Toe" in rv.data

    def test_make_move_route(self):
        rv = self.client.get('/make_move?x=0&y=0')
        assert rv.status_code == 302
        assert self.gs.get(0, 0) == GameState.CellUsedByPlayer1

    def test_reset_route(self):
        self.gs.load_from_string(" xoxxoxox")
        rv = self.client.get('/reset')
        assert rv.status_code == 302
        assert self.gs.is_empty()


if __name__ == '__main__':
    unittest.main()
