import numpy as np

def build_board(size):
    board = np.random.choice(['Empty', 'Red', 'Black'], size=(size, size))
    return board

def get_count(board, item):
    return np.count_nonzero(board == item)

if __name__ == "__main__":
    print("This file is not intended to be run as a main.")

def resize_board(board, new_size):
    if new_size < 4 or new_size > 16:
        raise ValueError("Invalid board size. Please enter a size between 4 and 16.")
    return np.resize(board, (new_size, new_size))

def pivot_board(board):
    return np.transpose(board)

