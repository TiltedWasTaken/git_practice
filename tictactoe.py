class TicTacToe:
    #Class variables:
    board_move = {"a1": "a1", "a2": "a2", "a3": "a3", "b1": "b1", 
    "b2": "b2", "b3": "b3", "c1": "c1", "c2": "c2", "c3": "c3"}
    def __init__(self, player = ""):
        self.player = player    
    def __repr__(self):
        return self.player
    win = False
    draw = False
    winner = ""    
    #Board Method
    def board(self, move = ""):


        if move != "" and self.player == "Player_One":
            TicTacToe.board_move[move] = " X"
        if move != "" and self.player == "Player_Two":
            TicTacToe.board_move[move] = " O"
            
        print("\n")
        print("   |   |   \n")
        print("" + TicTacToe.board_move["a1"] + " |" + TicTacToe.board_move["a2"] + " |" + TicTacToe.board_move["a3"] + " \n")
        print("_ _|_ _|_ _\n")
        print("   |   |   \n")
        print("" + TicTacToe.board_move["b1"] + " |" + TicTacToe.board_move["b2"] + " |" + TicTacToe.board_move["b3"] + " \n")
        print("_ _|_ _|_ _\n")
        print("   |   |   \n")
        print("" + TicTacToe.board_move["c1"] + " |" + TicTacToe.board_move["c2"] + " |" + TicTacToe.board_move["c3"] + " \n")
        print("   |   |   \n")
        print("\n")
    
    def move(self, move):
        self.board(move)
    def check_win(self):
        win_con_1 = TicTacToe.board_move["a1"], TicTacToe.board_move["a2"], TicTacToe.board_move["a3"]
        win_con_2 = TicTacToe.board_move["b1"], TicTacToe.board_move["b2"], TicTacToe.board_move["b3"]
        win_con_3 = TicTacToe.board_move["c1"], TicTacToe.board_move["c2"], TicTacToe.board_move["c3"]
        win_con_4 = TicTacToe.board_move["a1"], TicTacToe.board_move["b1"], TicTacToe.board_move["c1"]
        win_con_5 = TicTacToe.board_move["a2"], TicTacToe.board_move["b2"], TicTacToe.board_move["c2"]
        win_con_6 = TicTacToe.board_move["a3"], TicTacToe.board_move["b3"], TicTacToe.board_move["c3"]
        win_con_7 = TicTacToe.board_move["c1"], TicTacToe.board_move["b2"], TicTacToe.board_move["a3"]
        win_con_8 = TicTacToe.board_move["a1"], TicTacToe.board_move["b2"], TicTacToe.board_move["c3"]

        player_one_win = (" X", " X", " X")
        player_two_win = (" O", " O", " O")
        if win_con_1 == player_one_win or win_con_1 == player_two_win:
            TicTacToe.winner = self.player
            TicTacToe.win = True
        if win_con_2 == player_one_win or win_con_2 == player_two_win:
            TicTacToe.winner = self.player
            TicTacToe.win = True
        if win_con_3 == player_one_win or win_con_3 == player_two_win:
            TicTacToe.winner = self.player
            TicTacToe.win = True
        if win_con_4 == player_one_win or win_con_4 == player_two_win:
            TicTacToe.winner = self.player
            TicTacToe.win = True
        if win_con_5 == player_one_win or win_con_5 == player_two_win:
            TicTacToe.winner = self.player
            TicTacToe.win = True
        if win_con_6 == player_one_win or win_con_6 == player_two_win:
            TicTacToe.winner = self.player
            TicTacToe.win = True
        if win_con_7 == player_one_win or win_con_7 == player_two_win:
            TicTacToe.winner = self.player
            TicTacToe.wini = True
        if win_con_8 == player_one_win or win_con_8 == player_two_win:
            TicTacToe.winner = self.player
            TicTacToe.win = True   
        if TicTacToe.winner != "" and TicTacToe.win == True:
            print(TicTacToe.winner + " wins. \n" + "Game Over!\n")

        

    def check_draw(self):
        blank_count = 0
        values = TicTacToe.board_move.values()
        for value in values:
            if value != " X" and value != " O":
                blank_count += 1
        if blank_count == 0 and TicTacToe.win == False:
            TicTacToe.draw = True
            print("The game has finished as a draw.")
        
player_one = TicTacToe("Player_One")
player_two = TicTacToe("Player_Two")

player_one.move("b1")
player_one.move("b2")
player_one.move("b3")
player_one.check_win()

