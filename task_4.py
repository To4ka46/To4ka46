class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from an empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Peek from an emty stack")
        
    def is_empty(self):
        return len(self.stack) == 0
    
    #Пример:
s = Stack()
s.push(1)
s.push(2)
print(s.pop())
print(s.peek())