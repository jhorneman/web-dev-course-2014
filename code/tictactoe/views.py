from flask import render_template, redirect, request, url_for, abort,\
    session, flash, jsonify
from application import app, db
from models import GameState


@app.context_processor
def board_processor():
    def game_state_description(_gs):
        if _gs.state == GameState.Ongoing:
            if _gs.whose_turn_is_it == GameState.Player1:
                if session.get("player_id", None) == GameState.Player1:
                    return "It's your turn, player 1."
                else:
                    return "It's player 1's turn."
            elif _gs.whose_turn_is_it == GameState.Player2:
                if session.get("player_id", None) == GameState.Player2:
                    return "It's your turn, player 2."
                else:
                    return "It's player 2's turn."
            else:
                return "I don't know whose turn it is!"

        elif _gs.state == GameState.Player1Won:
            if session.get("player_id", None) == GameState.Player1:
                return "You have won!"
            else:
                return "Player 1 has won!"

        elif _gs.state == GameState.Player2Won:
            if session.get("player_id", None) == GameState.Player2:
                return "You have won!"
            else:
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


@app.route('/')
def index():
    game_id = session.get('game_id', None)
    if game_id:
        gs = GameState.query.get(game_id)
        if gs:
            return redirect(url_for('game', game_id=game_id))
        else:
            session["game_id"] = None
    return render_template('index.html')


@app.route('/new_game')
def new_game():
    gs = GameState()
    gs.nr_players = 1
    db.session.add(gs)
    db.session.commit()
    game_id = gs.id
    session["game_id"] = game_id
    session["player_id"] = GameState.Player1
    return redirect(url_for('game', game_id=game_id))


@app.route('/end_game')
def end_game():
    session["game_id"] = None
    session["player_id"] = None
    return redirect(url_for('index'))


@app.route('/api/is_it_my_turn_yet')
def is_it_my_turn_yet():
    result = "error"
    game_id_from_session = session.get("game_id", None)
    if game_id_from_session:
        gs = GameState.query.get(game_id_from_session)
        if gs:
            if gs.whose_turn_is_it == session.get("player_id", None):
                result = "yes"
            else:
                result = "no"
    return jsonify({"result": result})


@app.route('/game/<int:game_id>')
def game(game_id):
    gs = GameState.query.get_or_404(game_id)

    # Possible cases:
    # - I am the player of this game => play
    # - I am the player of no game
    #   - and this game has 1 player => join this game
    #   - else => index
    # - I am not a player of this game => index

    game_id_from_session = session.get("game_id", None)
    if game_id_from_session is None:
        assert gs.nr_players != 0
        if gs.nr_players == 1:
            gs.nr_players = 2
            db.session.commit()
            session["game_id"] = game_id
            session["player_id"] = GameState.Player2
            flash("You joined the game.")
        else:
            flash("This game already has two players.")
            return redirect(url_for('index'))

    elif game_id_from_session != game_id:
        flash("This is not your game.")
        return redirect(url_for('index'))

    is_it_my_turn = gs.whose_turn_is_it == session.get("player_id", None)

    return render_template('game.html', gs=gs, is_it_my_turn=is_it_my_turn)


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

    if x < 0 or x >= 3 or y < 0 or y >= 3:
        abort(400)

    game_id_from_session = session.get("game_id", None)
    if game_id_from_session != game_id:
        abort(400)

    if gs.whose_turn_is_it != session.get("player_id", None):
        abort(400)

    gs.make_move(x, y)
    db.session.commit()
    return redirect(url_for('game', game_id=game_id))
