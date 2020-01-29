rails = int(input())
for rail in range(rails):
    K, N, M = map(int, input().split())
    chargers = list(map(int, input().split()))
    busStops = [0]*N
    chargeGage = [0]*K
    for charger in chargers:
        busStops[charger] = 1
    minChargeNum = (N)//K
    try:
        if(minChargeNum == 0):
            raise Exception
        for busStop in busStops:
            chargeGage.pop()
            if(busStop==1):
                chargeGage = [0]*K
    except:
        minChargeNum = 0
    print("#{} {}".format(rail+1,minChargeNum))