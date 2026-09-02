class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1
    
    def push(self, color):
        if self.is_full():
            print("Stack is full")
            return False
        self.top += 1
        self.stack[self.top] = color
        return True

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        popped_color = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return popped_color

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def size(self):
        return self.top + 1

stack1 = Stack(5)
stack1.push("R")
stack1.push("G")
print(stack1.stack)
stack1.pop()
print(stack1.is_empty())
print(stack1.peek())
print(stack1.size())
print(stack1.is_full())