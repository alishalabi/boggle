from generate_board import generate_board
from prefix_tree import PrefixTree
from combinations import Combinations


class Game():
    def __init__(self, size=4):
        # Generate random game board
        self.game_board = generate_board(size)
        # Create dictionary with all English words
        self.dictionary = self.get_lines("/usr/share/dict/words")
        # Create empty prefix tree
        self.prefix_tree = PrefixTree()
        # Append each dictionary item to prefix tree
        for word in self.dictionary:
            self.prefix_tree.insert(word)
        # Create new combinations instance (using game_board)
        self.combination_instance = Combinations(self.game_board)
        self.all_combinations = self.combination_instance.all_searches()
        # Create empty array to store valid combinations
        self.valid_combinations = []

    # Read method inspired by https://github.com/Make-School-Courses/CS-2.1-Trees-Sorting/blob/master/Code/autocomplete.py
    def get_lines(self, filename="/usr/share/dict/words"):
        with open(filename) as file:
            lines = [line.strip() for line in file]
        return lines

    def solve(self):
        # Iterate through each combination
        for combination in self.all_combinations:
            if self.prefix_tree.contains(combination) == True:
                self.valid_combinations.append(combination)

    def print_solution(self):
        self.solve()
        print(f"All possible words for the following game board: {self.game_board}")
        # for word in self.valid_combinations:
        #     print(word)
        print(self.valid_combinations)


game = Game()
print(f"Combinations: {game.all_combinations}")
game.print_solution()
