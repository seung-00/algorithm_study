'''
이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이김. 즉, 횟수

ex)책이 총 400쪽. 검색구간의 왼쪽 l = 1, 오른쪽 r = 400, 중간 = c=int((l+r)/2)

찾는 쪽 번호가 c와 같아지면 탐색 종료.

이진 탐색 게임에서 이긴 사람이 누군지 알아내시오.  비긴 경우 0

----
계획.
A,B 한턴씩 실행해서 누가 먼저 찾나 실시 A다찾고 B다찾으면 시간증가 (DFS보단 BFS로)

'''

def BinarySearch(l,r,value): #1회 이진탐색 실시. return 값은 다음에 찾아야할 l,r 만약 값을 찾으면 True 반환
    c = int((l+r)/2)
    if c == value:
        return True
    else:
        if c<value:
            return c,r
        else:
            return l,c

test = int(input())
rstList = []
for _ in range(test):
    rst = ''
    P,cA,cB = map(int,input().split())
    lA =lB = 1
    rA =rB = P

    while True:
        resultA = BinarySearch(lA,rA,cA)
        resultB = BinarySearch(lB,rB,cB)

        if (resultA == True) and (resultB == True):
            rst = '0'
            break
        elif (resultA == True) and (resultB != True):
            rst = 'A'
            break
        elif (resultA != True) and (resultB == True):
            rst = 'B'
            break
        else:
            lA,rA = resultA
            lB,rB = resultB

    rstList.append(rst)

for t,rst in enumerate(rstList):
    print("#{} {}".format(t+1,rst))