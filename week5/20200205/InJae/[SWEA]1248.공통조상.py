test = int(input())


def FindCommonRoot(edge1, edge2, treeChild):
    edge1Ancestors = {}  # edge2의 값이 edge1에 있는지 탐색하는 것을 빠르게 하기 위해. listIdx로 참조하기엔 정점수는 최대 1만개임.
    curNode1 = edge1

    while curNode1 != 1:  # 부모노드가 1이 되기 전까지 탐색(rootNode정의). 최초 노드는 포함안하고 root노드는 포함해야 하므로  반복문 시작 시 부모노드를 현 노드로 업데이트.
        curNode1 = treeChild[curNode1]
        edge1Ancestors[curNode1] = True

    curNode2 = edge2
    while curNode2 not in edge1Ancestors:
        curNode2 = treeChild[curNode2]

    return curNode2

def CclSbTreeSize(rootNode,treePrt):
    if rootNode == None:
        return 0

    return 1 + CclSbTreeSize(treePrt[rootNode][0],treePrt) + CclSbTreeSize(treePrt[rootNode][1],treePrt)

for t in range(1,test+1):
    rst1 = 0  #가장 가까운 노드
    rst2 = 0 #조상노드의 수.
    nV,nE,edge1,edge2 = map(int,input().split())
    treePrt = [[None,None] for _ in range(nV+1)] #idx 부모노드, 리스트원소 : 자식노드   => 자식노드 기준 부모노드 찾기 힘듦.
    treeChild = [None for _ in range(nV+1)] #idx 자식노드. 리스트원소 : 부모노드

    pIdx = 0
    cIdx = 1
    inputList = list(map(int,input().split()))
    for _ in range(nV-1):
        p = inputList[pIdx]
        c = inputList[cIdx]

        if treePrt[p][0] is None:
            treePrt[p][0] = c
        else:
            treePrt[p][1] = c

        treeChild[c] = p

        pIdx += 2
        cIdx += 2

    commonNode = FindCommonRoot(edge1,edge2,treeChild)
    rst1 = commonNode
    rst2 = CclSbTreeSize(commonNode,treePrt)

    print("#{} {} {}".format(t,rst1,rst2))