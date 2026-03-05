from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise IndexError("Dequeue from an empty queue")
        
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Peek from an empty queue")
        
    def is_empty(self):
        return len(self.queue) == 0
    
    #Пример
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
print(q.peek()) 