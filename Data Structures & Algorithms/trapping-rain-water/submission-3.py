class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n
        result = 0
        pre = float("-inf")
        suf = float("-inf")
        for i in range(n):
            pre = max(pre, height[i])
            prefix[i] = pre
        for i in range(n-1 , -1 ,-1):
            suf = max(suf, height[i])
            suffix[i] = suf
        for i in range(n):
            num = min(suffix[i] , prefix[i])
            result += abs(height[i] - num)
        return result
