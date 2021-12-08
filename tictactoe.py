class TikTacToe:
    #Class variables:
    

    #Board Method
    def board(self):
        board_move = {"a1": " ", "a2": " ", "a3": " ", "b1": " ",
         "b2": " ", "b3": " ", "c1": " ", "c2": " ", "c3": " "}
        print("   |   |   \n")
        print(" " + board_move["a1"] + " | " + board_move["a2"] + " | " + board_move["a3"] + " \n")
        print("_ _|_ _|_ _\n")
        print("   |   |   \n")
        print(" " + board_move["b1"] + " | " + board_move["b2"] + " | " + board_move["b3"] + " \n")
        print("_ _|_ _|_ _\n")
        print("   |   |   \n")
        print(" " + board_move["c1"] + " | " + board_move["c2"] + " | " + board_move["c3"] + " \n")
        print("   |   |   \n")

prac = TikTacToe()

prac.board()