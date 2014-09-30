from flask import render_template, redirect, request, flash, url_for
from application import app
from models import GameState


# gs = GameState()
gs = GameState.create_from_string("xo x oxo  ")


@app.context_processor
def board_processor():
    def is_cell_empty(_gs, _x, _y):
        return _gs.board[_y][_x] == GameState.CellEmpty

    def cell_contents(_gs, _x, _y):
        if _gs.board[_y][_x] == GameState.CellUsedByPlayer1:
            return "X"
        elif _gs.board[_y][_x] == GameState.CellUsedByPlayer2:
            return "O"
        else:
            return ""

    return dict(
        is_cell_empty=is_cell_empty,
        cell_contents=cell_contents
    )


@app.route('/')
def index():
    global gs
    return render_template('index.html', gs=gs)
