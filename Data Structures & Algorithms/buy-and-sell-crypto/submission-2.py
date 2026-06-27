class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0] #10
        sell = 0 #0 , 4 , 5 , 6
        for i in range(1,len(prices)): # 1
            profit = prices[i] - buy # 1-1 =0
            sell = max(profit , sell) # 6
            buy = min(buy , prices[i]) # 1
        return sell