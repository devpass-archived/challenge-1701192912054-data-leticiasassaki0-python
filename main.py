class Stack:
    def __init__(self):
        // Add your solution here!

    def push(self, item):
        // Add your solution here!

    def pop(self):
        // Add your solution here!

    def peek(self):
        // Add your solution here!

    def is_empty(self):
        // Add your solution here!

    def size(self):
        // Add your solution here!

if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f'Pop: {stack.pop()}')  # Expected: 30
    print(f'Peek: {stack.peek()}')  # Expected: 20
    print(f'Is Empty: {stack.is_empty()}')  # Expected: False
    print(f'Size: {stack.size()}')  # Expected: 2
