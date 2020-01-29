class Solution:
    def __init__(self):
        self.cnt = 0

    def sol(self,x1,x2,x3,N):
        if x1+x2+x3 > N :
            return
        elif x1+x2+x3 == N:
            self.cnt += 1
            return
        else:
            self.sol(x1+20,x2,x3,N)
            self.sol(x1,x2+20,x3,N)
            self.sol(x1,x2,x3+10,N)


test = int(input())
rstList = []
for _ in range(test):
    N = int(input())
    s = Solution()
    s.sol(0,0,0,N)
    rst = s.cnt
    rstList.append(rst)

for t,rst in enumerate(rstList):
    print("#{} {}".format(t+1,rst))