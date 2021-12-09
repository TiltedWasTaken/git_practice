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

player_one.move("a2")
player_one.move("a1")
player_one.move("a3")
player_one.move("b1")
player_one.move("b2")
player_one.move("b3")
player_one.move("c1")
player_one.move("c2")
player_one.move("c3")

player_one.check_draw()