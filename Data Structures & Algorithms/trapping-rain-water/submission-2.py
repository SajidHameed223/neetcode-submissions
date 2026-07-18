class Solution:
    def trap(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = n * [0]
        suffix = n * [0]
        pre = nums[0]
        suf = nums[n-1]
        for i in range(n):
            pre = max(pre , nums[i])
            prefix[i] = pre
            suf = max(suf , nums[n-i-1])
            suffix[n-i-1] = suf
        result = 0 
        for i in range(n):
            result += min(suffix[i] , prefix[i]) - nums[i]
        return result