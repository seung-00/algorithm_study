test = int(input())
rstList = []


def DFS(r,c,table,visited):
    global rst
    visited[r][c] = True
    if table[r][c] == 3:
        rst = 1
        return
    else:
        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
            nr,nc = r+dr,c+dc
            if (0 <= nr < N) and (0 <= nc < N) and not visited[nr][nc]:
                if table[nr][nc] != 1:
                    DFS(nr,nc,table,visited)


for _ in range(test):
    N = int(input())
    table = [list(map(int,input())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    sPoint = [-1, -1]
    rst = 0
    for r in range(N):
        for c in range(N):
            if table[r][c] == 2:
                sPoint[0], sPoint[1] = r, c

    DFS(sPoint[0],sPoint[1],table,visited)

    rstList.append(rst)

for t,rst in enumerate(rstList):
    print("#{} {}".format(t+1,rst))