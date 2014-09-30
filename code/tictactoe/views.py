from flask import render_template, redirect, request, url_for, abort, current_app
from application import app
from models import GameState


@app.context_processor
def board_processor():
    def game_state_description(_gs):
        if _gs.state == GameState.Ongoing:
            if _gs.whose_turn_is_it == GameState.Player1:
                return "It's player 1's turn."
            elif _gs.whose_turn_is_it == GameState.Player2:
                return "It's player 2's turn."
            else:
                return "I don't know whose turn it is!"
        elif _gs.state == GameState.Player1Won:
            return "Player 1 has won!"
        elif _gs.state == GameState.Player2Won:
            return "Player 2 has won!"
        elif _gs.state == GameState.Draw:
            return "Draw!"
        else:
            return "Unknown state!"

    def is_cell_empty(_gs, _x, _y):
        return _gs.board[_y][_x] == GameState.CellEmpty

    def cell_contents(_gs, _x, _y):
        if _gs.board[_y][_x] == GameState.CellUsedByPlayer1:
            return "X"
        elif _gs.board[_y][_x] == GameState.CellUsedByPlayer2:
            return "O"
        else:
            return "&nbsp;"

    return dict(
        game_state_description=game_state_description,
        is_cell_empty=is_cell_empty,
        cell_contents=cell_contents
    )


@app.route('/')
def index():
    return render_template('index.html', gs=current_app.gs)


@app.route('/make_move')
def make_move():
    x = request.args.get('x', None)
    y = request.args.get('y', None)
    if x is None or y is None:
        abort(400)

    current_app.gs.make_move(int(x), int(y))
    return redirect(url_for('index'))


@app.route('/reset')
def reset():
    current_app.gs.reset()
    return redirect(url_for('index'))
