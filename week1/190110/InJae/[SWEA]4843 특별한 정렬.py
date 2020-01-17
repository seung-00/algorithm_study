'''
문제 이해
정렬인데, 큰수와 가장작은수, 2번째 큰수, 2번째 작은 수... 순으로 정렬하기

ex 1,2,3,4
   4,1,3,2

----
계획.
선택정렬을 이용하면 간단한 문제.
전체 arr에서 가장 큰수 찾기 -> 그 큰수를 제외한 나머지 부분의 큰 수는 2번째로 큰수가 됨
'''

test = int(input())

for t in range(test):
    numLen = int(input())
    numList = list(map(int,input().split()))

    turn = 1 #1이면 큰거할 차례 0이면 작은 놈 할 차례

    for i in range(10): #10개까지만 출력이므로 10번만 수행.
        if turn == 1:
            large = 0
            for j in range(i,numLen):
                if large < numList[j]:
                    large = numList[j]
                    largeIdx = j

            numList[i],numList[largeIdx] = numList[largeIdx], numList[i]
            turn = 0

        else:
            small = 101
            for j in range(i,numLen):
                if small > numList[j]:
                    small = numList[j]
                    smallIdx = j

            numList[i],numList[smallIdx] = numList[smallIdx], numList[i]
            turn = 1

    print("#"+str(t+1),*numList[:10])
    #print("#{} {}".format(t+1,*numList))