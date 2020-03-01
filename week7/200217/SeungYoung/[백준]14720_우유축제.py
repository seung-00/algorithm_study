def DP(milkShops):
    global dp
    if milkShops[0] == 0:
        dp[0][0] = 1
    for i in range(len(milkShops)):
        milk = milkShops[i]

        dp[i][0] = dp[i-1][2]+1 if milk == 0 else dp[i-1][0]
        dp[i][1] = dp[i-1][0]+1 if milk == 1 and dp[i][2]<dp[i][0] else dp[i-1][1]
        dp[i][2] = dp[i-1][1]+1 if milk == 2 and dp[i][0]<dp[i][1] else dp[i-1][2]


N = int(input())
milkShops = list(map(int, input().split()))
dp = [[0]*3 for i in range(N)]
DP(milkShops)
print(max(dp[N-1][0], dp[N-1][1], dp[N-1][2]))