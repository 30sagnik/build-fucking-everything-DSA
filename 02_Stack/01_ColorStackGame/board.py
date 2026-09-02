import random
from stack import Stack
class Board:
    def __init__(self, num_stacks, stack_capacity, colors):
        self.num_stacks = num_stacks
        self.stack_capacity = stack_capacity
        self.colors = colors
        self.stacks = []
        for _ in range(num_stacks):
            stack = Stack(stack_capacity)
            self.stacks.append(stack)

    #Move the color/ring from one stack to another
    def move_ring(self, source_stack_index, target_stack_index):
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

    def generate_rings(self):
        rings = []
        for ring in self.colors:
            for _ in range(self.stack_capacity):
                rings.append(ring)
                random.shuffle(rings)
        return rings

    def generate_random_board(self):
        rings = self.generate_rings()
        for ring in rings:
            while True:
                stack_index = random.randint(0, self.num_stacks - 1)
                if not self.stacks[stack_index].is_full():
                    self.stacks[stack_index].push(ring)
                    break

    def display_board(self):
        print("\nCurrent Board State:")
        for i, j in enumerate(self.stacks):
            print(f"{i+1}: {j.stack}")

    
    def check_win(self):
        for bar in self.stacks:
            organized = 0
            if not bar.is_empty():
                first_color = bar.peek()
                fill = 0
                for ring in bar.stack:
                    if ring == first_color:
                        fill +=1
                if fill == self.stack_capacity:
                    organized +=1

        if organized == len(self.colors):
            return True
        return False

board = Board(6, 6, ["R", "G", "B", "Y"])
board.generate_random_board()
print(board.display_board())
print(f"Win status: {board.check_win()}")

