# Combination code inspired by video blog: https://www.youtube.com/watch?v=aholjVetVDQ


sample_board = [['C', 'J', 'Z', 'E'], ['V', 'A', 'X', 'B'],
                ['X', 'N', 'T', 'U'], ['I', 'A', 'N', 'K']]

sample_dict = {"CAT", "DOG", "BYTE", "TUBE", "CAN", "ANT",
               "CAR", "TANK"}


class Combinations():
    def __init__(self, board=sample_board, dict=sample_dict):
        self.board = board
        self.dict = dict
        # Generate all neighbor coordinates for a given cell
        self.neighbor_coordinates = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0,  1),
            (1, -1),
            (1,  0),
            (1,  1),
        ]
        # Maintain array of ALL combinations (of length "length")
        self.all_combinations = []
        self.column_length = len(board[0])
        self.row_length = len(board)

    def get_neighbors(self, row_index, column_index):
        """
        For any given matrix cell, return list of all valid neighbors
        """
        all_neighbors = []
        # Move row and column indexes of each neighbor
        for neighbor in self.neighbor_coordinates:
            new_row = row_index + neighbor[0]
            new_column = column_index + neighbor[1]

            # Ensure that new row and column are both in matrix range
            if (new_row >= self.row_length) or (new_column >= self.column_length) or (new_column < 0) or (new_row < 0):
                continue
            # Append neighbor to array
            all_neighbors.append((new_row, new_column))  # neigh[2]
        return all_neighbors

    def depth_first_search(self, row, column, visited_array, current_combination, max_length=3):
        """
        Recursively search all available combinations for a single cell
        """
        # Exit scenario: Cell has been visited
        if (row, column) in set(visited_array):
            # self.all_combinations.append(current_combination)
            return
        # Exit scenario: current word is longer than max length parameter
        if len(current_combination) > max_length:
            # self.all_combinations.append(current_combination)
            return

        # Get new letter, append letter to visited array
        letter = self.board[row][column]
        visited_array.append((row, column))

        # Add letter to combination, append combination to all combinations
        current_combination += letter
        self.all_combinations.append(current_combination)

        # Recursively perform depth first search for each valid neighbor
        current_neighbors = self.get_neighbors(row, column)
        for neighbor in current_neighbors:
            self.depth_first_search(
                neighbor[0], neighbor[1], visited_array, current_combination, max_length=3)

    def all_searches(self):
        """
        Perform a depth first search for each cell in matrix
        """
        for row_index in range(self.row_length):
            for column_index in range(self.column_length):
                self.depth_first_search(row_index, column_index, [
                ], "")
        print(self.all_combinations)


combinations = Combinations()
combinations.all_searches()
