class Node:
    def __init__(self,data):
        self.node = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0 #링크드 리스트의 길이 반환.

    def addtoLast(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next_node != None:
                cur = cur.next_node
            cur.next_node = node
        self.len += 1

    def addtoFirst(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next_node = self.head
            self.head = node
        self.len += 1

    def add(self,data,idx):
        node = Node(data)
        if self.len<=idx: #Index Error(참조 범위 초과)
            return -1

        else:
            if idx == 0:
                self. addtoFirst(data)
            else:
                cur = self.head
                cnt = 0
                while cnt<idx-1:
                    cur = cur.next_node
                    cnt += 1
                temp_node = cur.next_node
                cur.next_node = node
                cur = cur.next_node
                cur.next_node = temp_node
        self.len+=1


    def delete(self,idx):
        if self.len<=idx:
            return -1
        else:
            cur = self.head
            cnt = 0
            while cnt<idx-1:
                cur = cur.next_node
                cnt += 1
            delNode = cur.next_node
            cur.next_node = delNode.next_node
        self.len -= 1

    def get(self,idx):
        if self.len<=idx:
            return -1
        else:
            cur = self.head
            cnt = 0
            while cnt<idx:
                cur = cur.next_node
                cnt += 1
            return cur.node

    def allPrint(self):
        if self.head == None:
            print("리스트에 값이 업습니다.")
        else:
            cur = self.head
            while cur != None:
                print(cur.node,end=" ")
                cur = cur.next_node
        print("\n")

test = int(input())
rstList = []
for _ in range(test):
    myList = LinkedList()
    N,M,L = map(int,input().split())
    numList = map(int,input().split())
    for n in numList:
        myList.addtoLast(n)
    for _ in range(M):
        idx,num = map(int,input().split())
        myList.add(num,idx)
    rst = myList.get(L)
    rstList.append(rst)

for t,rst in enumerate(rstList):
    print("#{} {}".format(t+1,rst))
