class Node:
    def __init__(self, value = None, pre = None, post = None):
        self.data = value
        self.pre = pre
        self.post = post

    def __str__(self):
        return str(self.data)


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def PopHead(self):
        if self.head == None:
            print("empty")
        else:
            self.head = self.head.post
            self.head.pre = None
            self.length -= 1

    def PopTail(self):
        if self.head == None:
            print("empty")
        else:
            self.tail = self.tail.pre
            self.tail.post = None
            self.length -= 1

    def InsertTail(self,data):
        if self.head == None:  # 시작
            newNode = Node(data, None, None)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(data, self.tail, None)
            self.tail.post = newNode
            self.tail = newNode
        self.length += 1

    def InsertHead(self,data):
        if self.head == None:  # 시작
            newNode = Node(data, None, None)
            self.head = newNode
            self.tail = newNode

        else:
            newNode = Node(data, None, self.head)
            self.head.pre = newNode
            self.head = newNode
        self.length += 1

    def GetByIdx(self, idx):
        if idx == 0:    return self.head
        elif idx == self.length-1:    return self.tail

        elif idx <= ((self.length-1)//2):  #앞에서부터
            cnt = 0
            cur = self.head
            while True:
                if idx == cnt:  break
                cur = cur.post
                cnt+=1
        else:   #뒤에서부터
            cnt = self.length-1
            cur = self.tail
            while True:
                if idx == cnt:
                    break
                cur = cur.pre
                cnt -= 1
        return cur


    def InsertByIdx(self,data, idx):
        if idx == 0:
            newNode = Node(data, None, self.head)
            self.head.pre = newNode
            self.head = newNode

        elif idx == self.length:
            newNode = Node(data, self.tail, None)
            self.tail.post = newNode
            self.tail = newNode

        else:
            target = self.GetByIdx(idx)
            newNode = Node(data, target.pre, target)
            target.pre.post = newNode
            target.pre = newNode
        self.length+=1



    def DisplayAll(self):
        cur = self.head

        while True :
            if cur.post == None:
                print(cur.data)
                break
            else:
                print(cur.data , "->", end=" ")
                cur = cur.post

#     answers.append(q.Dequeue())

# for t, answer in enumerate(answers):
#     print("#{} {}".format(t+1, answer))

TC = int(input())
for tc in range(1, TC+1):
    Dlist = DoubleLinkedList()
    N, M, L = map(int, input().split()) #수열의 길이 N, 추가 횟수 M, 출력할 인덱스 번호 L
    lst = list(map(int, input().split()))
    for _ in range(N):
        Dlist.InsertHead(lst.pop())
    for i in range(M):
        idx, val = map(int, input().split())
        Dlist.InsertByIdx(val, idx)
    print("#{} {}".format(tc, Dlist.GetByIdx(L)))


# k=DoubleLinkedList()

# k.InsertTail(3)

# k.InsertTail(4)

# k.InsertTail(5)

# k.InsertByIdx(100,0)

# k.DisplayAll()

# k.DisplayByIdx(1)
