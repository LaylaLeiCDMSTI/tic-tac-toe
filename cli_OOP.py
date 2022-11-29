# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

#from OOP_logic import tictactoe
from pandas_logic import tictactoe
from pandas_logic import games
if __name__ == '__main__':
    game = tictactoe()
    game.play()

print(games)