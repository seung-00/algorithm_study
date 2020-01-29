test = 10
for t in range(1,test+1):
    N = int(input())
    rst = 1
    valueList = []
    for _ in range(N):
        valueList.append(input().split())

    for values in valueList:
        if len(values) == 4:
            if values[1].isnumeric():
                rst = 0
                break

        else:
            if not values[1].isnumeric():
                rst = 0
                break
    print("#{} {}".format(t,rst))