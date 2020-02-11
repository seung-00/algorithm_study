d = [(0,1),(-1,0),(1,0),(-1,0)]
def FindMinVal(table,n):
    minVal = 987654321
    visited = set()

    for i in range(n):
        table[i] = 'x' + table[i] + 'x'
    table.insert(0,'x'*(n+2))
    table.append('x'*(n+2))

    n = n+2
    def _FindMinVal(r,c,table,n,val,visited): #pos = 현재위치 #table 맵 #n맵의 길이. -> 테이블 연장할 시! 길이
        nonlocal  minVal


        if minVal<=val:
            return
        else:
            if (r,c) == (n-2,n-2):
                minVal = val

        for dr,dc in d:
            cr = r+dr
            cn = c+dc
            if table[cr][cn] == 'x' or (cr,cn) in visited:
                continue
            _FindMinVal(cr,cn,table,n,val+int(table[cr][cn]),visited|{(cr,cn)}) #다음 위치에 대한 값을 넣어서 넘겨줌


    _FindMinVal(1,1,table,n,int(table[1][1]),visited)
    return minVal

test = int(input())
rstList = []
for _ in range(test):
    n = int(input())
    table = [input() for _ in range(n)]
    rstList.append(FindMinVal(table, n))
for t,rst in enumerate(rstList):
    print("#{} {}".format(t+1,rst))

