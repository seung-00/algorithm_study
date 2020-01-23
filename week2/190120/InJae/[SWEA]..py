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
    cheeseInput = map(int,input().split())
    cheeseQue = QUEUE(101)
    hwadukQue = QUEUE(N+1)

    for c in cheeseInput:
        cheeseQue.enQueue(c)

    for _ in range(N):
        hwadukQue.enQueue(cheeseQue.deQueue())

    remainP = N

    while remainP != 1:
        cheese = hwadukQue.deQueue()//2
        if cheese == 0 :
            if not cheeseQue.isEmpty():
                hwadukQue.que[hwadukQue.front] = cheeseQue.deQueue()
            else:
                remainP -= 1
        else:
            hwadukQue.que[hwadukQue.front] = cheese

    rst = 0
    for i,value in enumerate(hwadukQue.que):
        if value != 0:
           rst = i



    rstList.append(rst)

for t,rst in enumerate(rstList):
    print("#{} {}".format(t+1,rst))

