class Node:
    def __init__(self,data):
        self.node = data
        self.right = None
        self.left = None

class DList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertHead(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            curNode = self.head
            curNode.left = node
            node.right = curNode
            self.head = node

    def insertTail(self,value):
        node = Node(value)
        if self.tail is None:
            self.tail = node
            self.head = self.tail
        else:
            curNode = self.tail
            curNode.right = node
            node.left = curNode
            self.tail = node

    def deleteNodeHead(self):
        if self.head is None:
            return -1
        else:
            self.head = self.head.right
            self.head.left=None

    def deleteNodeTail(self):
        if self.tail is None:
            return -1
        else:
            self.tail = self.tail.left
            self.tail.right = None

    def printAll(self):
        cur = self.head

        while cur:
            print(cur.node)
            cur = cur.right

    def printLast(self):
        curNode = self.tail
        returnList = []
        for _ in range(10):
            if curNode is None:
                break
            returnList.append(curNode.node)
            curNode = curNode.left
        return returnList

    def sol(self,N,M,K):
        curNode = self.head
        for _ in range(K):
            flag = False
            for i in range(M):
                if i == M-1: #진행 중 tail에서 진행이 1번 남으면,
                    if curNode == self.tail:
                        self.insertTail(self.tail.node + self.head.node)
                        curNode = self.tail
                        flag = True
                        break
                 #그게 아니라면 쭉 이동하는데,
                if curNode == self.tail:  #만약에 현재노드가 끝지점이라면 현재노드는 처음지점.
                    curNode = self.head
                    continue
                else: #그 외의 경우라면 쭉 찾아봐
                    preNode = curNode
                    curNode = curNode.right
            if not flag:
                if curNode == self.head: #만약 현재노드가 맨 앞이라면,
                    self.insertHead(self.head.node) #맨앞 노드값 추가
                    curNode = self.head
                else:
                    node = Node(preNode.node+curNode.node) #앞쪽과 밀린값 더한 노드 생성

                    preNode.right = node
                    node.left = preNode

                    curNode.left = node
                    node.right = curNode

                    curNode = node
# myList = DList()
#
# for i in (6,2,4,9,1,5):
#     myList.insertTail(i)
#
# myList.sol(6,3,3)
# print(myList.printLast())

test = int(input())
for t in range(test):
    N,M,K = map(int,input().split())
    dList = DList()
    for i in map(int,input().split()):
        dList.insertTail(i)
    dList.sol(N,M,K)
    print("#{} ".format(t+1),end="")
    print(*dList.printLast())
