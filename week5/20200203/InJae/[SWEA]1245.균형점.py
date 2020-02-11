test = int(input())
rstList = []

def CclF(mgList,xObj):
    fLeft = 0
    fRight = 0

    for xMg,mMg in mgList:
        f = mMg/((xMg-xObj)**2)
        if xObj < xMg :
            fRight += f
        else:
            fLeft += f

    return fRight-fLeft #F알짜힘

for t in range(test):
    N = int(input())
    inputList=list(map(int,input().split()))
    mgList = []
    xIdx = 0
    mIdx = N
    for i in range(N):
        mgList.append((inputList[xIdx],inputList[mIdx]))
        xIdx += 1
        mIdx += 1

    mgList.sort()
    balancePoints = []

    for i in range(N-1):
        l = mgList[i][0]
        r = mgList[i+1][0]

        rep = 0
        while rep < 100 :
            mid = (l+r)/2 #물체 위치

            F = CclF(mgList,mid)

            if F<0 :
                l = mid
            elif F>0 :
                r = mid
            else:
                break
            rep += 1
        balancePoints.append(mid)
    print("#"+str(t+1),end = " ")
    for i in range(N-1):
        print("%.10f"%(balancePoints[i]), end =" ")
    print("")