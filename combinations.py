# Combination code inspired by video blog: https://www.youtube.com/watch?v=aholjVetVDQ

from generate_board import generate_board


class Combinations():
    def __init__(self, board, prefix_tree):
        self.board = board
        self.prefix_tree = prefix_tree
        # Generate all neighbor coordinates for a given cell
        self.neighbor_coordinates = [
            (-1, -1),  # Up left
            (-1, 0),  # Up
            (-1, 1),  # Up right
            (0, -1),  # Left
            (0,  1),  # Right
            (1, -1),  # Down left
            (1,  0),  # Down
            (1,  1),  # Down right
        ]
        # Maintain array of ALL combinations (of length "length")
        self.all_combinations = set()
        self.column_length = len(board[0])
        self.row_length = len(board)

    def get_neighbors(self, row_index, column_index):
        """
        For any given matrix cell, return list of all valid neighbors
        """
        all_neighbors = []
        # Move row and column indexes of each neighbor
        for row_offset, column_offset in self.neighbor_coordinates:
            new_row = row_index + row_offset
            new_column = column_index + column_offset

            # Ensure that new row and column are both in matrix range
            if (0 <= new_row < self.row_length and  # Row is valid index
                    0 <= new_column < self.column_length):  # Column is valid index
                # Append neighbor to array
                all_neighbors.append((new_row, new_column))  # neigh[2]
        return all_neighbors

    def depth_first_search(self, row, column, visited_path, current_combination):
        """
        Recursively search all available combinations from a single cell
        """
        # # Exit scenario: Cell has been visited
        # if (row, column) in visited_path:
        #     # self.all_combinations.add(current_combination)
        #     return

        # Get new letter, append letter to visited array
        letter = self.board[row][column]
        visited_path.append((row, column))

        # Add letter to combination, append combination to all combinations
        current_combination += letter
        # Check if the current combination is a valid dictionary word
        if self.prefix_tree.contains(current_combination):
            # Sets do not allow duplicate elements
            self.all_combinations.add(current_combination)

        # Check if the current combination is a prefix of any dictionary words
        completions = self.prefix_tree.complete(current_combination)
        if len(completions) == 0:
            return

        # Recursively perform depth first search for each valid neighbor
        current_neighbors = self.get_neighbors(row, column)
        for neighbor in current_neighbors:
            # Skip neighbor cell if it has been visited
            if neighbor not in visited_path:
                self.depth_first_search(
                    neighbor[0], neighbor[1], visited_path.copy(), current_combination)

    def all_searches(self):
        """
        Perform a depth first search for each cell in matrix
        """
        for row_index in range(self.row_length):
            for column_index in range(self.column_length):
                self.depth_first_search(row_index, column_index, [], "")
        # print(self.all_combinations)
        return self.all_combinations


# board = generate_board()
# print(board)
# combinations = Combinations(board)
# print(combinations.all_searches())
