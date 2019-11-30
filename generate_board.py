import random
import string


def generate_board(size=4):
    # Instantiate new array
    board = [[random.random() for i in range(size)] for j in range(size)]
    print(board)


generate_board()
