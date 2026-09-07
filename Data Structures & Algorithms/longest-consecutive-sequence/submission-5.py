class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        ans = 0 
        for num in hashmap:
            res = 0 
            if num - 1 not in hashmap:
                while num + res in hashmap:
                    res += 1
            ans = max(ans , res)
        return ans 