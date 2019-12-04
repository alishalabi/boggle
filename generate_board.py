import random
import string


def generate_board(size=4):
    # Instantiate new array
    board = [[random.choice(string.ascii_lowercase)
              for i in range(size)] for j in range(size)]
    return board
