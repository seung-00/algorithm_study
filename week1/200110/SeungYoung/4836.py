testNum = int(input())
for test in range(testNum):
    graph = [['' for i in range(10)] for j in range(10)]
    nums = int(input())
    for num in range(nums):
        edge = list(map(int, input().split()))
        color = edge.pop()
        ptX = list([edge[0], edge[2]])
        ptY = list([edge[1], edge[3]])
        points = [(x,y) for x in range(ptX[0],ptX[1]+1) for y in range(ptY[0],ptY[1]+1)]
        for point in points:
            if(graph[point[0]][point[1]]): #다른 색 있음
                graph[point[0]][point[1]] = False
            elif(graph[point[0]][point[1]] == ''): #아직 안 칠 함
                graph[point[0]][point[1]] = color
        overlap = [1 for i in range(len(graph)) for j in range(len(graph[0])) if graph[i][j] == False]
    print("#{} {}".format(test+1,sum(overlap)))