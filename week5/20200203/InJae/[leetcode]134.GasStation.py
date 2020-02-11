class Solution2:
    def canCompleteCircuit(self, gas, cost) :
        n = len(gas)
        for sIdx in range(n):
            day = 0
            amountGas = 0
            flag = True
            curIdx = sIdx
            while day<n:
                amountGas += gas[curIdx]
                if amountGas-cost[curIdx] >= 0:
                    amountGas-=cost[curIdx]
                    day += 1
                    curIdx = (curIdx + 1) % n
                else:
                    flag = False
                    break
            if flag:
                return sIdx
        return -1


class Solution:
    def canCompleteCircuit(self, gas, cost):

        if sum(gas) - sum(cost) < 0:
            return -1

        tank = 0
        s = 0
        tot = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:  # if empty
                s = i + 1
                tot += tank
                tank = 0

        else:
            return s
s = Solution()
gas= [1,2,3,4,5]
cost = [3,4,5,1,2]
print(s.canCompleteCircuit(gas,cost))