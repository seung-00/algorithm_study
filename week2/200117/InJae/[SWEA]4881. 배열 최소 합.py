def DFS(r,pre_c,table,N,value):
    global min
    if value>min:
        return

    if r>=N:
        if min>value:
            min = value
        return

    for c in range(N):
        c = str(c)
        if c in pre_c:
            continue
        else:
            DFS(r + 1, pre_c +c, table, N, value + table[r][int(c)])


test = int(input())
rstList= []
for _ in range(test):
    min = 999999999
    N = int(input())
    table = [list(map(int,input().split())) for _ in range(N)]
    DFS(0,'',table,N,0)
    rstList.append(min)

for t,rst in enumerate(rstList):
    print("#{} {}".format(t+1,rst))