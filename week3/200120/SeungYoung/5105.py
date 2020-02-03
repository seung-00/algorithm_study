TC = int(input())
#상하좌우
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

for tc in range(1, TC+1):
    n = int(input())
    maze = [list(map(int, list(input()))) for _ in range(n)]
    queue = []
    visit = [[False] * n for _ in range(n)]
    distance = [[0]*n for _ in range(n)]
    result = 0

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                queue.append((i, j))
                visit[i][j] = True # 출발 지점
    
    while queue:
        x, y = queue.pop(0) # now
        
        for i in range(4):
            if maze[x][y] == 3:
                result = distance[x][y] - 1
                break


            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if (not visit[nx][ny]) and (maze[nx][ny] != 1):
                    queue.append((nx, ny))
                    visit[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1


    print('#{} {}'.format(tc, result))