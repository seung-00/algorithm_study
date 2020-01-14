'''
문제 이해
1~12까지 숫자를 가진 집합 A {1,2,3,...,12}

문제 목표
집합 A의 부분 집합 중 N개의 원소를 가지고 있고, 원소의 합이 K인 부분집합의 갯수를 구하라.

point.
N개의 원소를 가지고 있는 부분집합 구하기.


110111
111111

110111 1<<(i&j)
'''



test = int(input())
rstList = []

A = [1,2,3,4,5,6,7,8,9,10,11,12]
for _ in range(test):
    N,K = map(int,input().split())
    rst = 0
    for num in range(1<<12):
        cnt = 0 # N과 수가 같은지 확인
        for i in range(12):
            if num & (1<<i) : cnt += 1
            if cnt > N:
                break

        if cnt != N:
            continue

        else:
            total = 0
            for i in range(12):
                if num & (1<<i):
                    total += A[i]

            if total == K :
                rst += 1

    rstList.append(rst)

for t,rst in enumerate(rstList):
    print("#{} {}".format(t+1,rst))