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

def BFS(que,visited,N,table):
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    while not que.isEmpty():
        while not que.isEmpty():
            r,c,cnt = que.deQueue()
            if table[r][c] == 3:
                return cnt
            visited[r][c] = True
            for i in range(4):
                nr,nc = r+dr[i],c+dc[i]
                if 0<=nr<N and 0<=nc<N :
                    if table[nr][nc] != 1 and not visited[nr][nc]:
                        que.enQueue([nr,nc,cnt+1])

    return 0
test = int(input())
rstList = []
for _ in range(test):
    N = int(input())
    table = [list(map(int,input())) for _ in range(N)]
    startPoint = [-1,-1,-1]

    for r in range(N):
        for c in range(N):
            if table[r][c] == 2:
                startPoint[0],startPoint[1] = r,c

    visited = [[False for _ in range(N)] for _ in range(N)]
    que = QUEUE(1000)
    que.enQueue(startPoint)


    rstList.append(BFS(que,visited,N,table))

for t,rst in enumerate(rstList):
    print("#{} {}".format(t+1,rst))

