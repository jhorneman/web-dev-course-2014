from application import db


class GameState(db.Model):
    # Possible states for the entire game
    Ongoing = 0
    Player1Won = 1
    Player2Won = 2
    Draw = 3

    # Possible states for each _board cell
    CellEmpty = 0
    CellUsedByPlayer1 = 1
    CellUsedByPlayer2 = 2

    # Player indices
    Player1 = 0
    Player2 = 1


    id = db.Column(db.Integer, primary_key=True)
    nr_players = db.Column(db.Integer)
    whose_turn_is_it = db.Column(db.Integer)
    board = db.Column(db.String)    # TODO: Find a way to limit this to 9 characters
    state = db.Column(db.Integer)


    def __init__(self):
        self.reset()

    def reset(self):
        self.nr_players = 0
        self.whose_turn_is_it = GameState.Player1
        self.board = "         "
        self.update_state()

    def get(self, _x, _y):
        assert _x >= 0 and _x < 3
        assert _y >= 0 and _y < 3

        index = _y * 3 + _x

        if self.board[index] == 'x':
            return GameState.CellUsedByPlayer1
        elif self.board[index] == 'o':
            return GameState.CellUsedByPlayer2
        else:
            return GameState.CellEmpty

    def set(self, _x, _y, _new_cell_value):
        assert _x >= 0 and _x < 3
        assert _y >= 0 and _y < 3

        index = _y * 3 + _x

        if _new_cell_value == GameState.CellUsedByPlayer1:
            char = 'x'
        elif _new_cell_value == GameState.CellUsedByPlayer2:
            char = 'o'
        else:
            char = ' '

        self.board = self.board[:index] + char + self.board[index+1:]

    def is_ongoing(self):
        return self.state == GameState.Ongoing

    def make_move(self, _x, _y):
        assert self.state == GameState.Ongoing
        assert _x >= 0 and _x < 3
        assert _y >= 0 and _y < 3
        assert self.get(_x, _y) == GameState.CellEmpty

        if self.whose_turn_is_it == GameState.Player1:
            self.set(_x, _y, GameState.CellUsedByPlayer1)
            self.whose_turn_is_it = GameState.Player2
        else:
            self.set(_x, _y, GameState.CellUsedByPlayer2)
            self.whose_turn_is_it = GameState.Player1

        self.update_state()

    def update_state(self):
        self.state = GameState.Ongoing

        # Check rows
        for i in xrange(3):
            v = self.get(0, i)
            if v != GameState.CellEmpty:
                if self.get(1, i) == v and \
                   self.get(2, i) == v:
                    self.set_state_based_on_cell(v)
                    return

        # Check columns
        for i in xrange(3):
            v = self.get(i, 0)
            if v != GameState.CellEmpty:
                if self.get(i, 1) == v and \
                   self.get(i, 2) == v:
                    self.set_state_based_on_cell(v)
                    return

        # Check first diagonal
        v = self.get(0, 0)
        if v != GameState.CellEmpty:
            if self.get(1, 1) == v and \
               self.get(2, 2) == v:
                self.set_state_based_on_cell(v)
                return

        # Check second diagonal
        v = self.get(2, 0)
        if v != GameState.CellEmpty:
            if self.get(1, 1) == v and \
               self.get(0, 2) == v:
                self.set_state_based_on_cell(v)
                return

        # Check if _board is full
        for i in xrange(3):
            for j in xrange(3):
                if self.get(j, i) == GameState.CellEmpty:
                    return

        self.state = GameState.Draw

    def set_state_based_on_cell(self, _cell_value):
        if _cell_value == GameState.CellUsedByPlayer1:
            self.state = GameState.Player1Won
        elif _cell_value == GameState.CellUsedByPlayer2:
            self.state = GameState.Player2Won
        else:
            assert False

    def is_empty(self):
        for i in xrange(3):
            for j in xrange(3):
                if self.get(j, i) != GameState.CellEmpty:
                    return False
        return True

    def load_from_string(self, _init_string):
        self.board = _init_string.lower()
        self.update_state()

    @staticmethod
    def create_from_string(_init_string):
        gs = GameState()
        gs.load_from_string(_init_string)
        return gs
