TC = int(input())
#상하좌우
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

for tc in range(1, TC+1):
    n = int(input())
    maze = [list(map(int, list(input()))) for _ in range(n)]
    result = 0

    stack = []
    visit = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                stack.append((i, j))
                visit[i][j] = True # 출발 지점
    
    while stack:
        x, y = stack.pop() # now
       
        if maze[x][y] == 3:
            result = 1
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if (not visit[nx][ny]) and (maze[nx][ny] != 1):
                    stack.append((nx, ny))
                    visit[nx][ny] = True

    print('#{} {}'.format(tc, result))
