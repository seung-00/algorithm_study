def DFS(start, visited = 0):
    global rst
    visited += pow(2, start)
    for nextNode in range(1, V+1):
        # 1. 연결된 노드인가 2. 방문 안 한 노드인가
        if graphTable[start][nextNode] and not visited&(1<<nextNode):
            if nextNode == goal:
                rst = 1
                return
            else: DFS(nextNode)


tc = int(input())
for c in range(tc):
    rst = 0

    #다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
    V,E = map(int,input().split())

    #인접 행렬 만들기
    graphTable = [list(0 for i in range(V+1)) for j in range(V+1)]
    
    for _ in range(E):
        startV, endV = map(int,input().split())
        graphTable[startV][endV] = 1
    start, goal = map(int,input().split())
    DFS(start)
    print("#{} {}".format(c+1, rst))
