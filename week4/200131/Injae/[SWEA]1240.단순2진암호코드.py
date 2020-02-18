import sys
input = sys.stdin.readLine().rstrip()
test = int(input())
rstList = []
deCodeNum = {'0001101' : 0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6,'0111011':7,'0110111':8,'0001011':9}

def Search(table,N,M): #끝이 1인 값을 찾는 함수 input : table  return :1이 시작하는 i,j값
    i = 0
    j = M-1
    while (table[i][j] != '1'):
        i += 1
        if i == N:
            j -= 1
            i = 0
    return (i,j)

def Decode(i,j,table): #암호 끝위치의 테이블에서 7자리씩 값을 받아 numList에 값을 넣어주는 함수.
    numList = [0]*8
    j -= 55

    for numIdx in range(8):
        num = table[i][j:j+7]
        numList[numIdx] = deCodeNum[num]
        j+=7

    return numList

def DetectCode(numList):
    val = numList[1]+numList[3]+numList[5]+numList[7]+ (numList[0]+numList[2]+numList[4] + numList[6])*3
    if val%10 == 0 :
        return sum(numList)
    else:
        return 0

for _ in range(test):
    N,M = map(int,input().split())
    table = [input() for _ in range(N)]
    rst = 0
    i,j = Search(table,N,M)
    numList = Decode(i,j,table)
    rst = DetectCode(numList)
    rstList.append(rst)

for t,rst in enumerate(rstList):
    print("#{} {}".format(t+1,rst))