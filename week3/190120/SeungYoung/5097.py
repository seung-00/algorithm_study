class CircularQueue:
    def __init__(self, max):
        self.max = max+1
        self.queue = [None]*(self.max)
        self.size = self.front = self.rear = 0

    def GetNextIdx(self, idx):
        return (idx+1) % self.max

    def IsEmpty(self):
        return self.size == 0

    def IsFull(self):
        return self.GetNextIdx(self.rear) == self.front

    def Enqueue(self, item):
        if self.IsFull():
            print("Q is fulled")
            return False
        self.rear = self.GetNextIdx(self.rear)
        self.queue[self.rear] = item
        self.size += 1
        return True
    
    def Dequeue(self):
        if self.IsEmpty():
            print("Q is empty")
            return False
        self.front = self.GetNextIdx(self.front)
        return self.queue[self.front]

    def Peek(self):
        return self.queue[self.GetNextIdx(self.front)]
    
    def Display(self):
        cur = self.front
        while cur != self.rear:
            cur = self.GetNextIdx(cur)
            print(self.queue[cur])


8