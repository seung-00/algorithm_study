class Solution:
    def maxProfit(self, prices) :
        N = len(prices)
        i = 0
        total = 0
        curStockPrice = 0
        if (prices[i]<prices[i+1]):
            curStockPrice = prices[i]
        i += 1
        if N == 3:
            while i < N - 1:
                if prices[i - 1] > prices[i] and prices[i + 1] > prices[i]:
                    curStockPrice = prices[i]
                elif prices[i - 1] < prices[i] and prices[i + 1] < prices[i]:
                    total += prices[i] - curStockPrice
                break
        else:
            while i<N-2:
                if prices[i-1]>prices[i] and prices[i+1]>prices[i]:
                    curStockPrice = prices[i]
                elif prices[i-1]<prices[i] and prices[i+1]<prices[i]:
                    total += prices[i]-curStockPrice
                i += 1

        if prices[i] < prices[i+1]:
            total += prices[i+1]-curStockPrice
        else:
            if curStockPrice != 0:
                total += prices[i] - curStockPrice
            else:
                pass


        return total
s = Solution()
print(s.maxProfit([2,1,4]))

