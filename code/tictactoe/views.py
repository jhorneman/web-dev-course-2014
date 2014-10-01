from flask import render_template, redirect, request, url_for, abort, current_app, g, session
from application import app, db
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
        return _gs.get(_x, _y) == GameState.CellEmpty

    def cell_contents(_gs, _x, _y):
        if _gs.get(_x, _y) == GameState.CellUsedByPlayer1:
            return "X"
        elif _gs.get(_x, _y) == GameState.CellUsedByPlayer2:
            return "O"
        else:
            return "&nbsp;"

    return dict(
        game_state_description=game_state_description,
        is_cell_empty=is_cell_empty,
        cell_contents=cell_contents
    )


# @app.before_request
# def get_game_state():
#     if not hasattr(g, "gs"):
#         gamestate_id = session.get('gamestate_id', None)
#         if gamestate_id is None:
#             gs = GameState()
#             db.session.add(gs)
#             db.session.commit()
#             gamestate_id = gs.id
#             session["gamestate_id"] = gamestate_id
#         else:
#             gs = GameState.query.filter(GameState.id == gamestate_id).first()
#             if not gs:
#                 gs = GameState()
#                 db.session.add(gs)
#                 db.session.commit()
#                 gamestate_id = gs.id
#                 session["gamestate_id"] = gamestate_id
#         g.gs = gs


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/new_game')
def new_game():
    gs = GameState()
    db.session.add(gs)
    db.session.commit()
    game_id = gs.id
    session["game_id"] = game_id
    return redirect(url_for('game', game_id=game_id))


@app.route('/game/<int:game_id>')
def game(game_id):
    gs = GameState.query.get_or_404(game_id)
    return render_template('game.html', gs=gs)


@app.route('/game/<int:game_id>/make_move')
def make_move(game_id):
    gs = GameState.query.get_or_404(game_id)

    x = request.args.get('x', None)
    y = request.args.get('y', None)
    if x is None or y is None:
        abort(400)

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        abort(400)

    if x >= 0 and x < 3 and y >= 0 and y < 3:
        gs.make_move(x, y)
        db.session.commit()
        return redirect(url_for('game', game_id=game_id))
    else:
        abort(400)
