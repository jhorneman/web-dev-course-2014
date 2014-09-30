
class GameState(object):
	# Possible states for the entire game
	Ongoing = 0
	Player1Won = 1
	Player2Won = 2
	Draw = 3

	# Possible states for each board cell
	CellEmpty = 0
	CellUsedByPlayer1 = 1
	CellUsedByPlayer2 = 2

	# Player indices
	Player1 = 0
	Player2 = 1

	def __init__(self):
		self.reset()

	def reset(self):
		self.whose_turn_is_it = GameState.Player1
		self.board = [
			[GameState.CellEmpty for j in xrange(3)]
				for i in xrange(3)
		]
		self.update_state()

	def is_ongoing(self):
		return self.state == GameState.Ongoing

	def make_move(self, _x, _y):
		assert self.state == GameState.Ongoing
		assert _x >= 0 and _x < 3
		assert _y >= 0 and _y < 3
		assert self.board[_y][_x] == GameState.CellEmpty

		if self.whose_turn_is_it == GameState.Player1:
			self.board[_y][_x] = GameState.CellUsedByPlayer1
			self.whose_turn_is_it = GameState.Player2
		else:
			self.board[_y][_x] = GameState.CellUsedByPlayer2
			self.whose_turn_is_it = GameState.Player1

		self.update_state()

	def update_state(self):
		self.state = GameState.Ongoing

		# Check rows
		for i in xrange(3):
			v = self.board[i][0]
			if v != GameState.CellEmpty:
				if self.board[i][1] == v and \
				   self.board[i][2] == v:
					self.set_state_based_on_cell(v)
					return

		# Check columns
		for i in xrange(3):
			v = self.board[0][i]
			if v != GameState.CellEmpty:
				if self.board[1][i] == v and \
				   self.board[2][i] == v:
					self.set_state_based_on_cell(v)
					return

		# Check first diagonal
		v = self.board[0][0]
		if v != GameState.CellEmpty:
			if self.board[1][1] == v and \
			   self.board[2][2] == v:
				self.set_state_based_on_cell(v)
				return

		# Check second diagonal
		v = self.board[0][2]
		if v != GameState.CellEmpty:
			if self.board[1][1] == v and \
			   self.board[2][0] == v:
				self.set_state_based_on_cell(v)
				return

		# Check if board is full
		for i in xrange(3):
			for j in xrange(3):
				if self.board[i][j] == GameState.CellEmpty:
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
				if self.board[i][j] != GameState.CellEmpty:
					return False
		return True

	def load_from_string(self, _init_string):
		init_string = _init_string.lower()
		for i in xrange(9):
			if init_string[i] == 'x':
				self.board[i // 3][i % 3] = GameState.CellUsedByPlayer1
			elif init_string[i] == 'o':
				self.board[i // 3][i % 3] = GameState.CellUsedByPlayer2
		self.update_state()

	@staticmethod
	def create_from_string(_init_string):
		gs = GameState()
		gs.load_from_string(_init_string)
		return gs


if __name__ == "__main__":
	gs1 = GameState()
	gs1.make_move(0, 0)

	gs2 = GameState.create_from_string("xoxoxoxxo")
