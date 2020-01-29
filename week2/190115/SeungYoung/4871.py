def DFS(graph, node, goal, visited = []):
    if node not in visited:
        if(node == goal):
            return True
        visited.append(node)
    for neighbour in graph[node] - set(visited):
        if(DFS(graph, neighbour, goal, visited)):
            return True

tc = int(input())
for case in range(tc):
    ve = list(map(int, input().split()))
    graph = {v:set() for v in range(1,ve[0]+1)}
    for e in range(ve[1]):
        route = list(map(int, input().split()))
        graph[route[0]].add(route[1])
    root, goal = map(int, input().split())
    print("#{} ".format(case+1),end='')
    if(DFS(graph, root, goal)):
        print(1)
    else:
        print(0)