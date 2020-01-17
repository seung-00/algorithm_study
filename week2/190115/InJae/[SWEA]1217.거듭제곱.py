def pow(a,x):
    if x == 0:
        return 1
    else:
        return a*pow(a,x-1)

for _ in range(10):
    t = int(input())
    a,x = map(int,input().split())
    rst = pow(a,x)

    print("#{} {}".format(t,rst))
