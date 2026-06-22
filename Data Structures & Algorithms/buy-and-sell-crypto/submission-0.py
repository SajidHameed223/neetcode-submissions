class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        buy = nums[0]
        profit = 0 
        for i in range(len(nums)):
            temp = nums[i] - buy 
            profit = max(temp , profit)
            buy = min(buy , nums[i])
        return profit            