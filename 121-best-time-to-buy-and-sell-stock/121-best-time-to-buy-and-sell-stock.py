class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit =0
        i=0
        for j in range(len(prices)):
            if prices[i]>prices[j]:
                i=j
            else:
                profit = max(profit,prices[j]-prices[i])
        return profit
        
        