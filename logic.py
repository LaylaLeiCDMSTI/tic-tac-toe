# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def start_player():
    return input("choose to start as 'X' or 'O':")

def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    #player = "X"
    row = 3
    col = 3
    winCheck = True
    check = []
    rowCheck = []
    colCheck = []
    diaCheck = [[],[]]
    #put roll in check list
    for i in range(row):
        rowCheck.append(board[i])
    #print(rowCheck)

    #put colume in check list 
    cols = zip(rowCheck[0],rowCheck[1],rowCheck[2])
    colCheck = list(cols)

    #print(check)
    #put diagonal in check list
    #print(diaCheck)
    for i in range(row):
        for j in range(col):
            if i == j:
                diaCheck[0].append(board[i][j])
            if i == 2-j:
                diaCheck[1].append(board[i][2-j])
    #print(diaCheck)

    check = rowCheck + colCheck + diaCheck
    #print(check)

    for pos in check:
        if pos[0] == pos[1] == pos[2]:
            winCheck = True
            print("player", pos[0], "wins the game")
            return pos[0]
    if None not in pos:
            winCheck = False
            print("Draw")
            return 'Draw'
    #return None  # FIXME


def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == "X":
        player = "O"
        print("O's turn")
        return player
    if player == "O":
        player = "X"
        print("X's turn")
        return player
