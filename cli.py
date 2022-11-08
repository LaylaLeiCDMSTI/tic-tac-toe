# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import start_player
from logic import get_winner
from logic import other_player

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    Player = start_player()
    while winner == None:
        print("TODO: take a turn!")
        print("player", Player)
        # TODO: Show the board to the user.
        for c in board:
            print(c)
        # TODO: Input a move from the player.
        
        x = int(input("please input x value(1-3) of cell you want to place:"))
        if x<1 or x>3:
                x = int(input("Invalide input, try again:"))
        y = int(input("please input y value(1-3) of cell you want to place:"))
        if y<1 or y>3:
                y = int(input("Invalide input, try again:"))

        # TODO: Update the board.
        if board[x-1][y-1] == None:
            board[x-1][y-1] = Player
            winner = get_winner(board)
            Player = other_player(Player)
        else: 
            print("The cell has been taken, choose another one.")
        for c in board:
            print(c)
        # TODO: Update who's turn it is.
        winner = get_winner(board)
        #Player = other_player(Player)

        #winner = 'X'  # FIXME