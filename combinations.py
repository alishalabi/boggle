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
            (-1, -1, "↖"),
            (-1, 0, "↑"),
            (-1, 1, "↗"),
            (0, -1, "←"),
            (0,  1, "→"),
            (1, -1, "↙"),
            (1,  0, "↓"),
            (1,  1, "↘"),
        ]
        # Maintain array of ALL combinations (of length "length")
        self.all_combinations = []
        self.column_length = len(board[0])
        self.row_length = len(board)

    def get_neighbors(self, row_index, column_index):
        all_neighbors = []
        # Move row and column indexes of each neighbor
        for neighbor in self.neighbor_coordinates:
            new_row = row_index + neighbor[0]
            new_column = column_index + neighbor[1]

            # Ensure that new row and column are both in matrix range
            if (new_row >= row_length) or (new_column >= column_length) or (new_column < 0) or (new_row < 0):
                continue
            # Append neighbor to array
            all_neighbors.append(new_row, new_column, neigh[2])
        return all_neighbors

    def depth_first_search(self, row, columm, visited_array, current_combination, direction, max_length=3):
        # Exit scenario: Cell has been visited
        if (row, column) in visited_array:
            # print(f"Current combination: {current_combination}")
            self.all_combinations.append(current_combination)
            return
        # Exit scenario: current word is longer than max length parameter
        if len(current_combination) > max_length:
            # print(f"Current combination: {current_combination}")
            self.all_combinations.append(current_combination)
            return

        letter = board[row][column]
        visited.append((row, column))

        current_combination += letter

        current_neighbors = get_neighbors(row, column)
        for neighbord in current_neighbors:
            depth_first_search(
                neighbor[0], neighbor[1], visited_array[::], current_combination, direction + " " + neighbor[2], max_length=3)

    def all_searches(self):
        for row_index in range(self.board[0]):
            for column_index in range(self.board):
                depth_first_search(self, row_index, column_index, [
                ], "", 'directions from ({},{})({}) go '.format(row_index, column_index, letter))
        print(all_combinations)


combinations = Combinations()
combinations.all_searches()
