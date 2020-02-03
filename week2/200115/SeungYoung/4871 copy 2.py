def DFS(graph, node, goal, visited = []):
    if(node == goal):
        return True
    visited.append(node)
    childNode = list((graph[node]) - set(visited))   #자식 노드 중 아직 안 간 곳
    while childNode:
        if(DFS(graph, childNode.pop(), goal, visited)):
            return True


tc = int(input())
for case in range(tc):
    ve = list(map(int, input().split()))
    graph = {v:set() for v in range(1,ve[0]+1)}
    #{1:(4, 2, 3) 2: () ... }

    for e in range(ve[1]):
        route = list(map(int, input().split()))
        graph[route[0]].add(route[1])

    root, goal = map(int, input().split())
    if DFS(graph, root, goal):
        print(1)
#    print("#{} {}".format(case+1, int(DFS(graph, root) ) ) )