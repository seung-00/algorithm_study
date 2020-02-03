'''
문제 이해
10*10의 격자에 빨간색과 파란색 색칠.

문제 목표.
칠이 끝난 후 겹쳐 보라색이 된 칸 수 구하기

input :
최상단 testcase 수

1.칠할 영역의 갯수
2.칠하는 방식 2 2 4 4 1 ([2,2]~[4,4]까지 color1로 색칠)

계획 작성
color1인 값의 집합과 color 2인 값의 집합 구해서 공통집합 찾으면 되는 일인데,
부분집합 구하기 연산을 배웠으니 그것을 이용하여 접근.

부분집합 구할 때 하나씩 다 체크했었음. i*(1<<j)

따라서 여기서도 이와 비슷한 방식으로 접근

10*10 checkTable을 만들고 해당 값은 0->색칠x 1->빨강 2-> 블루 3->보라
1칠하려는데 2칠해져있으면 rst += 1
'''

def FindAr(x1,y1,x2,y2): #return 칠할 영역 리스트
    return [(i,j) for i in range(x1,x2+1) for j in range(y1,y2+1)]

def ApplyTable(table,r,c,color): #return 칠한 테이블 및 중복 여부
    overlap = 0
    if table[r][c] == 0 :
        table[r][c] = color
    elif table[r][c] != color :
        overlap = 1
        table[r][c] = 3
    else:
        pass

    return table, overlap


test = int(input())
rstList = []
for _ in range(test):
    table = [[0 for _ in range(10)] for _ in range(10)]
    rst = 0

    numApply = int(input())
    for _ in range(numApply):
        x1,y1,x2,y2,color = map(int,input().split())
        for r,c in FindAr(x1,y1,x2,y2):
            table,overlap = ApplyTable(table,r,c,color)
            rst+=overlap


    rstList.append(rst)


for t,rst in enumerate(rstList):
    print("#{} {}".format(t+1,rst))
