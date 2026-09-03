from board import Board

def get_valid_bar_index(board, prompt):
    while True:
        try:
            index = int(input(prompt)) - 1
            if 0 <= index < len(board.stacks):
                return index
            else:
                print(f"Invalid bar index. Please enter a number between [1:{len(board.stacks)}]")
        except ValueError:
            print("Please enter a valid integer.")

def main():
    board = Board(6, 6, ["R", "G", "B", "Y"])
    board.generate_random_board()
    step_count = 0

    while True:
        board.display_board()
        source_index = get_valid_bar_index(board, "Enter the source bar index (1-6): ")
        target_index = get_valid_bar_index(board, "Enter the target bar index (1-6): ")
        if board.move_ring(source_index, target_index):
            step_count += 1
            print(f"Moved ring from Bar {source_index +1} to Bar {target_index +1}.\nSteps taken: {step_count}")
        if board.check_win():
            board.display_board()
            print("Congratulations! You have won the game!")
            print(f"Total steps taken: {step_count}")
            break

if __name__ == "__main__":
    print("Welcome to the Color Stack Game!")
    print("Objective: Move the colored rings to form stacks of a single color.")
    main()