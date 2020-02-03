class Stack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("stack is empty")
            return

    def isEmpty(self):
        if self.stack:
            return True
        else:
            return False

    def peek(self):
        if self.stack:
            return stack[-1]
        else:
            return False

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

for _ in range(3):
    print("pop item =>", stack.pop())