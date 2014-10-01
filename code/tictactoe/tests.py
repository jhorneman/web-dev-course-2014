import unittest
import json
from flask import session
from models import GameState
from application import create_app
from create_db import create_db


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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False
app.config['SECRET_KEY'] = 'sekrit!'


class WebTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            create_db(app.db)

    def create_game(self):
        with app.app_context():
            gs = GameState()
            gs.nr_players = 1
            app.db.session.add(gs)
            app.db.session.commit()
            return gs.id

    def test_index_page(self):
        rv = self.client.get('/')
        assert "Tic Tac Toe" in rv.data
        assert "Start a game" in rv.data

    def test_index_redirects_to_current_game(self):
        game_id = self.create_game()
        with self.client.session_transaction() as s:
            s['game_id'] = game_id
            s['player_id'] = GameState.Player1
        rv = self.client.get('/', follow_redirects=True)
        assert "Tic Tac Toe" in rv.data
        assert "your turn" in rv.data

    def test_index_handles_non_existent_game(self):
        with self.client as c:
            with self.client.session_transaction() as s:
                s['game_id'] = 2
                s['player_id'] = GameState.Player1
            rv = c.get('/', follow_redirects=True)
            assert "Tic Tac Toe" in rv.data
            assert "Start a game" in rv.data
            assert session['game_id'] is None

    def test_new_game(self):
        with self.client as c:
            rv = c.get('/new_game', follow_redirects=True)
            assert "Tic Tac Toe" in rv.data
            assert "your turn" in rv.data
            assert session['game_id'] is 1
            assert session['player_id'] is GameState.Player1

    def test_end_game(self):
        with self.client as c:
            with self.client.session_transaction() as s:
                s['game_id'] = 1
                s['player_id'] = GameState.Player1
            rv = c.get('/end_game', follow_redirects=True)
            assert "Tic Tac Toe" in rv.data
            assert "Start a game" in rv.data
            assert session['game_id'] is None
            assert session['player_id'] is None

    def test_is_it_my_turn_yet_api_when_its_my_turn(self):
        game_id = self.create_game()
        with self.client as c:
            with self.client.session_transaction() as s:
                s['game_id'] = game_id
                s['player_id'] = GameState.Player1
            rv = c.get('/api/is_it_my_turn_yet', follow_redirects=True)
            response = json.loads(rv.data)
            assert 'result' in response
            assert response['result'] == 'yes'

    def test_is_it_my_turn_yet_api_when_its_not_my_turn(self):
        game_id = self.create_game()
        with self.client as c:
            with self.client.session_transaction() as s:
                s['game_id'] = game_id
                s['player_id'] = GameState.Player2
            rv = c.get('/api/is_it_my_turn_yet', follow_redirects=True)
            response = json.loads(rv.data)
            assert 'result' in response
            assert response['result'] == 'no'

# TODO: Test /game route
# TODO: Test /make_move route


if __name__ == '__main__':
    unittest.main()
