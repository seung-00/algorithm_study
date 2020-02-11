Decode = {'0001101' : 0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6,'0111011':7,'0110111':8,'0001011':9}


def CheckPwd(numList):
    if ((numList[0] + numList[2] + numList[4] + numList[6])*3 + numList[1]+numList[3]+numList[5]+numList[7])%10 == 0:
        return sum(numList)
    else:   return 0

def Search(table,N,M):
    i = 0
    j = M-1
    while (table[i][j] != '1'):
        i += 1
        if i == N:
            j -= 1
            i = 0
    return (i,j)


def GetPwd(table, i, j): # 끝의 i, j => (마지막 행, 첫 번째 열로 이동해서 찾음)
    rstList = [0]*8
    j -= 55

    for rstIdx in range(8):
        pw = table[i][j:j+7]
        rstList[rstIdx] = Decode[pw]
        j+=7
    return rstList



def DetectCode(numList):
    val = numList[1]+numList[3]+numList[5]+numList[7]+ (numList[0]+numList[2]+numList[4] + numList[6])*3
    if val%10 == 0 :
        return sum(numList)
    else:
        return 0

rst = []

tc = int(input())
for c in range(tc):
    N,M = map(int,input().split())
    table = [input() for _ in range(N)]
    endRow, endCol = Search(table, N, M)
    codes = GetPwd(table,endRow, endCol)
    rst.append(CheckPwd(codes))

for t,rst in enumerate(rst):
    print("#{} {}".format(t+1,rst))