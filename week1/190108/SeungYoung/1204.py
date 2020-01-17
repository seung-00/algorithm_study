cases = int(input())
for case in range(cases):
    temp = int(input())
    scores = list(map(int, input().split()))
    scoreCnts = [0]*101
    for score in scores:
        scoreCnts[score] = scoreCnts[score]+1
    maxCnt,maxCntScore = 0,0
    for i in range(101):
        if(maxCnt == scoreCnts[i] and maxCntScore<i):
            maxCntScore = i
        elif(maxCnt<scoreCnts[i]):
            maxCnt = scoreCnts[i]
            maxCntScore = i
    print("#{} {}".format(temp,maxCntScore))