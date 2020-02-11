class Node:
    def __init__(self,left=None,right=None,val=None):
        self.left = left
        self.right = right
        self.val = val

class BinaryTree:
    def __init__(self):
        self.root = None
        self.cnt = 0
    
    def InsertRoot(self, val):
        rootNode = Node(None, None, val)
        self.root = rootNode

    def Insert(self, parentVal, left, right):
        if left:
            self.TraversalAndInsert(self.root, parentVal, left)
        if right:
            self.TraversalAndInsert(self.root, parentVal, right)


    def TraversalAndInsert(self, node, parentVal, childVal):
        if node == None: return
        elif node.val == parentVal:
            childNode = Node(None, None, childVal)
            if node.left == None: node.left = childNode
            else: node.right = childNode
            return
        self.TraversalAndInsert(node.left, parentVal, childVal)
        self.TraversalAndInsert(node.right, parentVal, childVal)

    def Count(self, subTreeRootVal):
        self.TraversalAndCount(self.root, subTreeRootVal)
        return self.cnt

    def TraversalAndCount(self, node, subTreeRootVal):
        if node == None: return
        elif node.val == subTreeRootVal:
            self.CountSubtree(node)
            return
        self.TraversalAndCount(node.left, subTreeRootVal)
        self.TraversalAndCount(node.right, subTreeRootVal)

    def CountSubtree(self, node):
        if node == None: return
        self.cnt+=1
        self.CountSubtree(node.left)
        self.CountSubtree(node.right)



tc = int(input())
for case in range(1, tc+1):
    E, N = map(int, input().split())
    BTree = BinaryTree()

    temp = list(map(int,input().split()))
    root = temp[0]

    BTree.InsertRoot(root)
    graph = {p:[] for p in range(1,E+2)}

    for _ in range(E):
        p, c = temp.pop(0), temp.pop(0)
        graph[p].append(c)
    
    slot = [root]
    while slot:
        parentVal = slot.pop()
        if len(graph[parentVal]) == 2:
            child_1 = graph[parentVal][0]
            child_2 = graph[parentVal][1]
        elif len(graph[parentVal]) == 1:
            child_1 = graph[parentVal][0]
            child_2 = None
        else: continue
        BTree.Insert(parentVal, child_1, child_2)
        
        if child_1: slot.append(child_1)
        if child_2: slot.append(child_2)
    
    print("#{} {}".format(case, BTree.Count(N)))