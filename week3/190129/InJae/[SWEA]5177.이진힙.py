    class HEAP:
        def __init__(self,N):
            self.heap = [0 for _ in range(N+1)]
            self.numNodes = 0

        def Insert(self,item):
            self.numNodes+=1
            i = self.numNodes
            while self.heap[i//2] > item :
                self.heap[i] = self.heap[i//2]
                i//=2
            self.heap[i] = item

    test = int(input())
    rstList = []

    for _ in range(test):
        N = int(input())
        inputNums = map(int,input().split())
        heap = HEAP(N)
        for n in inputNums:
            heap.Insert(n)
        rst = 0
        lst = N
        while lst>0 :
            rst+=heap.heap[lst//2]
            lst//=2
        rstList.append(rst)

    for t,rst in enumerate(rstList):
        print("#{} {}".format(t+1,rst))