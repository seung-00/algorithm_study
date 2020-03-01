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


    def MergeByMax(self, otherList):
        cur = self.head

        for i in range(self.length+1):
            if i == self.length: break  # otherlist head 보다 큰 값이 없는 경우, i = length
            elif cur.data > otherList.head.data:   break
            cur = cur.post

        # 앞뒤로 넣기만 하면 되는 경우
        if i == 0:
            otherList.tail.post = self.head
            self.head.pre = otherList.tail
            self.head = otherList.head

        elif i == self.length:
            otherList.head.pre = self.tail
            self.tail.post = otherList.head
            self.tail = otherList.tail

        # 중간에 끼워야 하는 경우
        else:
            otherList.head.pre = cur.pre
            cur.pre.post = otherList.head

            otherList.tail.post = cur
            cur.pre = otherList.tail
        self.length = self.length + otherList.length

    def DisplayAllReverse(self):
        cur = self.tail

        for _ in range(10) :
            if cur.pre == None:
                print(cur.data, end='')
                break
            else:
                print(cur.data , end=" ")
                cur = cur.pre
        print()

    def DisplayAll(self):
        cur = self.head

        while True :
            if cur.post == None:
                print(cur.data)
                break
            else:
                print(cur.data, "->", end=" ")
                cur = cur.post


TC = int(input())
for tc in range(1, TC+1):
    rstDList = DoubleLinkedList()
    N, M = map(int, input().split())
    #수열의 길이 N, 수열의 개수 M, 이후 M개의 줄에 걸쳐 1000이하의 자연수로 구성된 수열
    tempList = list(map(int, input().split()))
    for val in tempList:
        rstDList.InsertTail(val)

    for _ in range(M-1):
        tempList = list(map(int, input().split()))
        tempDList = DoubleLinkedList()
        for val in tempList:
            tempDList.InsertTail(val)
        rstDList.MergeByMax(tempDList)
#        rstDList.DisplayAll()
    print("{}{} ".format("#",tc),end='')
    rstDList.DisplayAllReverse()
