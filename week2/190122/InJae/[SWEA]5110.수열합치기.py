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

    def appendList(self,apList): #apList는 더블리스트
        value = apList.head.node
        curNode = self.head
        flag = False
        while True:
            if curNode == self.tail:
                if curNode.node > value:
                    flag = True
                break
            if curNode.node>value:
                flag = True
                break
            preNode = curNode
            curNode = curNode.right

        if curNode == self.tail and not flag:
            lstNode = self.tail
            lstNode.right = apList.head
            apList.head.left = lstNode
            self.tail = apList.tail

        elif curNode == self.head: ##self.head넣는 과정없음.
            curNode.left = apList.tail
            apList.tail.right = curNode
            self.head = apList.head


        else:
            apList.head.left = preNode
            preNode.right = apList.head
            apList.tail.right = curNode
            curNode.left = apList.tail

    def printLast(self):
        curNode = self.tail
        returnList = []
        for _ in range(10):
            returnList.append(curNode.node)
            curNode = curNode.left
        return returnList

# myList1 = DList()
# myList2 = DList()
# myList3 = DList()
# myList4 = DList()
# for i in (2,3,4,5):
#     myList1.insertTail(i)
#
# for i in (4,8,7,6):
#     myList2.insertTail(i)
#
# for i in (9,10,15,16):
#     myList3.insertTail(i)
#
# for i in (1,2,6,5):
#     myList4.insertTail(i)
#
# myList1.appendList(myList2)
# myList1.appendList(myList3)
# myList1.appendList(myList4)

test= int(input())
for t in range(test):
    N,M = map(int,input().split())
    csdList = DList()
    for i in map(int,input().split()):
        csdList.insertTail(i)

    for _ in range(M-1):
        nextList = DList()
        for i in map(int,input().split()):
            nextList.insertTail(i)

        csdList.appendList(nextList)

    print("#{}".format(t+1),end =" ")
    print(*csdList.printLast())