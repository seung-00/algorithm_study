
#공통 조상 찾기
def FindParent(graph, son, mySet):
    for p in list(graph.keys()):
        if son in graph[p]:
            mySet.add(p)
            FindParent(graph, p, mySet)

def FindCommonParent(graph, son, mySet, otherSet):
    for p in list(graph.keys()):
        if son in graph[p]:
            if Primising(p, otherSet):  
                mySet.add(p)
                return
            else: FindCommonParent(graph, p, mySet, otherSet)


def Primising(myP, otherSet):
    if myP in otherSet: return True
    else: return False
    
def CountSubSet(graph, subSetRoot):
    #BFS
    que = []
    que.append(subSetRoot)
    cnt = 0
    while que:
        child = que.pop(0)
        cnt+=1
        que.extend(graph[child])
    return cnt

tc = int(input())
for case in range(1, tc+1):
    #각 케이스의 첫줄에는 트리의 정점의 총 수 V와 간선의 총 수 E, 공통 조상을 찾는 두 개의 정점 번호가 주어진다 (정점의 수 V는 10 ≤ V ≤ 10000 이다). 
    V, E, R1, R2 = map(int, input().split())

    temp = list(map(int,input().split()))
    root = temp[0]

    graph = {p:[] for p in range(1,V+1)}

    for _ in range(E):
        p, c = temp.pop(0), temp.pop(0)
        graph[p].append(c)
    
    setR1 = set()
    setR2 = set()

    FindParent(graph, R1, setR1)
    FindCommonParent(graph, R2, setR2, setR1)
    subSetRoot = setR2.pop()
    print("#{} {} {}".format(case, subSetRoot, CountSubSet(graph, subSetRoot)))