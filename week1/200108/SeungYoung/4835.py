cases = int(input())
for case in range(cases):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    max, min = 0, sum(nums)
    cnt = N-M+1
    for i in range(cnt):
        tempSum = sum(nums[i:M+i])
        if(max<tempSum): max = tempSum
        if(min>tempSum): min = tempSum
    print("#{} {}".format(case+1,max-min))