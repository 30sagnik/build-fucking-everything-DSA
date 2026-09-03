import random
from stack import Stack
class Board:
    def __init__(self, num_stacks = 6, stack_capacity = 6, colors = None):
        if colors is None:
            colors = ["R", "G", "B", "Y"]
        self.num_stacks = num_stacks
        self.stack_capacity = stack_capacity
        self.colors = colors
        self.stacks = []
        for _ in range(num_stacks):
            stack = Stack(stack_capacity)
            self.stacks.append(stack)

    #Move the color/ring from one stack to another
    def move_ring(self, source_stack_index, target_stack_index):
        if source_stack_index == target_stack_index:
            print("Source and Target Bar indices are same. Choose Different Bars")
            return False
        if source_stack_index < 0 or source_stack_index >= len(self.stacks):
            print("Invalid source stack index")
            return False
        if target_stack_index < 0 or target_stack_index >= len(self.stacks):
            print("Invalid target stack index")
            return False
        source_stack = self.stacks[source_stack_index]
        target_stack = self.stacks[target_stack_index]
        if source_stack.is_empty():
            print("Source stack is empty. Cannot move ring.")
            return False
        if target_stack.is_full():
            print("Target stack is full. Cannot move ring.")
            return False
        target_stack.push(source_stack.pop())
        return True

    #Generate a list of rings based on the colors and stack capacity
    def generate_rings(self):
        rings = []
        for color in self.colors:
            # for _ in range(self.stack_capacity):
            #     rings.append(ring)
            rings.extend([color] * self.stack_capacity)
        random.shuffle(rings)
        return rings

    #Generate a random board by distributing the rings across the stacks
    def generate_random_board(self):
        rings = self.generate_rings()
        for ring in rings:
            while True:
                stack_index = random.randint(0, self.num_stacks - 1)
                if not self.stacks[stack_index].is_full():
                    self.stacks[stack_index].push(ring)
                    break

    #Display the current state of the board
    def display_board(self):
        print("\n========Current Board State========")
        for level in range(self.stack_capacity, 0, -1):
            row=""
            for bar in self.stacks:
                items = bar.get_items()
                if level <= len(items):
                    row += f"| {items[level - 1]} | "
                else:
                    row += "|   | "
            print(row)
        print("----- "*len(self.stacks))
        labels = []
        for i in range(len(self.stacks)):
            labels.append(f"Bar{i+1} ".center(6))
        print(" "+"".join(labels))

    #Check if the game is won by verifying if all stacks are either empty or homogenous
    def check_win(self):
        completed_stacks = 0
        for bar in self.stacks:
            if bar.is_empty():
                continue
            elif bar.is_homogenous():
                completed_stacks += 1
            else:
                return False
        return completed_stacks == len(self.colors)

if __name__ == "__main__": #--QUICK TESTING
    board = Board(6, 6, ["R", "G", "B", "Y"])
    board.generate_random_board()
    board.display_board()
    board.move_ring(0, 1)
    board.display_board()
    board.move_ring(1, 2)
    board.display_board()
    board.move_ring(2, 3)
    board.move_ring(2, 3)
    board.move_ring(2, 4)
    board.move_ring(2, 4)
    board.move_ring(2, 5)
    board.move_ring(2, 5)
    board.move_ring(2, 1)
    board.move_ring(2, 1)
    board.display_board()
    print(f"Win status: {board.check_win()}")

