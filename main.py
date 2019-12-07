from pprint import pprint

from generate_board import generate_board
from prefix_tree import PrefixTree
from combinations import Combinations


class Game():
    def __init__(self, size=4):
        # Generate random game board
        self.game_board = generate_board(size)
        pprint(self.game_board)
        # Create dictionary with all English words
        print("Reading dictionary words...")
        self.dictionary = self.get_lines("/usr/share/dict/words")
        print(f"Read {len(self.dictionary)} dictionary words from file")
        # Create empty prefix tree
        print("Building prefix tree...")
        self.prefix_tree = PrefixTree()
        # Append each dictionary item to prefix tree
        for word in self.dictionary:
            # TEMP HACK until get better Boggle dictions: Skip one-letter 'words'
            if len(word) > 1:
                self.prefix_tree.insert(word)
        print(f"Built prefix tree with {self.prefix_tree.size} dictionary words")
        # Create new combinations instance (using game_board)
        print("Searching for all combinations...")
        self.combination_instance = Combinations(
            self.game_board, self.prefix_tree)
        self.all_combinations = self.combination_instance.all_searches()
        print(f"Generated {len(self.all_combinations)} valid word combinations")
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
            if self.prefix_tree.contains(combination) is True:
                self.valid_combinations.append(combination)

    def print_solution(self):
        print("Finding valid combinations...")
        self.solve()
        # print(f"All possible words for the following game board: {self.game_board}")
        # for word in self.valid_combinations:
        #     print(word)
        print(f"{len(self.valid_combinations)} valid combinations: {sorted(self.valid_combinations)}")


def main():
    game = Game()
    sorted_combos = sorted(game.all_combinations)
    start_letters = sorted(set(combo[0] for combo in sorted_combos))
    partitioned_combos = [[combo for combo in sorted_combos if combo.startswith(letter)]
                          for letter in start_letters]

    # # Generic template for list comprensions:
    # list_comprehension = [item for item in collection]
    # # Exactly equivalent to this unwrapped code:
    # list_comprehension = []
    # for item in collection:
    #     list_comprehension.append(item)
    print(f"All combinations:")
    for combos in partitioned_combos:
        start_letter = combos[0][0]
        print(f"{len(combos)} combos starting at {start_letter!r}: {combos}")
    # print(f" Prefix tree: {game.prefix_tree}")
    game.print_solution()
    # game.print_solution()


if __name__ == '__main__':
    main()
