# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
import random


class tictactoe:

    def __inti__(self):
        print("Game start")

    def get_board(self):
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        return board

    def start_player(self):
        mode = int(input("type 1 to play with a bot \ntype 2 to play with another player"))
        if mode == 1:
            return 'B'
        else:
            return input("choose to start as 'X' or 'O':")

    def get_winner(self,board):
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
            if pos[0] == pos[1] == pos[2] and pos[0] != None:
                winCheck = True
                print("player", pos[0], "wins the game")
                return pos[0]
        boardlist = []
        for n in board:
            for m in n:
                boardlist.append(m)
        if None not in boardlist:
                winCheck = False
                print("Draw")
                return 'Draw'
        #return None  # FIXME

    def play(self):
        board = self.get_board()
        winner = None
        Player = self.start_player()
        if Player == 'B':
            while winner == None:
                print("TODO: take a turn!")
                print("Your turn")
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
                bx = self.bot_choice()
                by = self.bot_choice()
                # TODO: Update the board.
                if board[x-1][y-1] == None:
                    board[x-1][y-1] = 'P'
                    winner = self.get_winner(board)
                    while board[bx-1][by-1] != None:
                        winner = self.get_winner(board)
                        if winner == "Draw" or winner == "P" or winner == "B":
                            return
                        else:
                            bx = self.bot_choice()
                            by = self.bot_choice()

                    board[bx-1][by-1] = 'B'
      
                else: 
                    print("The cell has been taken, choose another one.")
                
                for c in board:
                    print(c)
            # TODO: Update who's turn it is.
                winner = self.get_winner(board)
            #Player = other_player(Player)
        else:
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
                    winner = self.get_winner(board)
                    Player = self.other_player(Player)
                else: 
                    print("The cell has been taken, choose another one.")
                for c in board:
                    print(c)
                winner = self.get_winner(board)


    def other_player(self):
        """Given the character for a player, returns the other player."""
        if player == "X":
            player = "O"
            print("O's turn")
            return player
        if player == "O":
            player = "X"
            print("X's turn")
            return player

    def bot_choice(self):
        num = random.randint(1,3)
        return num
