class TicTacToe:
    #Class variables:
    def __init__(self, player = ""):
        self.player = player    
    def __repr__(self):
        return self.player
    #Board Method
    def board(self, move = ""):
        board_move = {"a1": " ", "a2": " ", "a3": " ", "b1": " ",
         "b2": " ", "b3": " ", "c1": " ", "c2": " ", "c3": " "}

        if move != "" and self.player == "Player_One":
            board_move[move] = "X"
        if move != "" and self.player == "Player_Two":
            board_move[move] = "O"

        print("   |   |   \n")
        print(" " + board_move["a1"] + " | " + board_move["a2"] + " | " + board_move["a3"] + " \n")
        print("_ _|_ _|_ _\n")
        print("   |   |   \n")
        print(" " + board_move["b1"] + " | " + board_move["b2"] + " | " + board_move["b3"] + " \n")
        print("_ _|_ _|_ _\n")
        print("   |   |   \n")
        print(" " + board_move["c1"] + " | " + board_move["c2"] + " | " + board_move["c3"] + " \n")
        print("   |   |   \n")
    
    def move(self, move):
        self.board(move)

        
player_one = TicTacToe("Player_One")
player_two = TicTacToe("Player_Two")

player_one.move("a2")

