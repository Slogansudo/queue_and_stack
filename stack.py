
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("ERROR: Stack is empty")

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(20)
stack.push(30)
stack.push(40)

print("stack:", stack.items)

stack.pop()
print("stack:", stack.items)

print(stack.is_empty())

print(stack.size())


