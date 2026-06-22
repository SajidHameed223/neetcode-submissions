class Solution:
    def trap(self, nums: List[int]) -> int:
        n = len(nums)
        output = 0
        prefix = [0] * n 
        suffix = [0] * n 
        prefix[0] = nums[0]
        for i in range(n):
            prefix[i] = max(prefix[i-1] , nums[i])
        suffix[n-1] = nums[n-1]
        for i in range(n-2 , -1 ,-1):
            suffix[i] = max(suffix[i+1] , nums[i])
        for i in range(n):
            output += min(prefix[i] , suffix[i]) - nums[i]
        return output     