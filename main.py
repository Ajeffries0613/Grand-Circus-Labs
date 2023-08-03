from checkers import build_board, get_count, resize_board, pivot_board

def game():
    size = int(input("Enter the square board size (minimum 4, maximum 16): "))
    if size < 4 or size > 16:
        print("Invalid board size. Please enter a size between 4 and 16.")
        return

    board = build_board(size)
    print("\nRandom Board:")
    print(board)

    print("\nNumber of Empty cells:", get_count(board, 'Empty'))
    print("Number of Red cells:", get_count(board, 'Red'))
    print("Number of Black cells:", get_count(board, 'Black'))

    new_size = int(input("\nEnter the new size for the board: "))
    try:
        resized_board = resize_board(board, new_size)
        print("\nResized Board:")
        print(resized_board)

        pivoted_board = pivot_board(board)
        print("\nPivoted Board:")
        print(pivoted_board)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    game()
