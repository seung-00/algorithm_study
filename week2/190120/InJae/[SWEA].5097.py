class QUEUE:
    def __init__(self,MAX_SIZE):
        self.que_len = MAX_SIZE
        self.que = [0 for _ in range(MAX_SIZE)]
        self.rear = 0
        self.front = 0

    def isEmpty(self):
        if self.rear == self.front:
            return True
        else:
            return False

    def isFull(self):
        if (self.rear+1)%self.que_len == self.front:
            return True
        else:
            return False

    def enQueue(self,item):
        self.rear = (self.rear+1)%self.que_len
        self.que[self.rear] = item

    def deQueue(self):
        self.front = (self.front+1)%self.que_len
        return self.que[self.front]

    def Peek(self):
        return self.que[(self.front+1)%self.que_len]

test = int(input())
rstList = []
for _ in range(test):
    N,M = map(int,input().split())
    que = QUEUE(100)
    numList = map(int,input().split())
    for n in numList:
        que.enQueue(n)
    for _ in range(M):
        que.enQueue(que.deQueue())

    rstList.append(que.Peek())

for t,rst in enumerate(rstList):
    print("#{} {}".format(t+1,rst))

