class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        res = 0
        for num in hashmap:
            count = 1
            while num + count in hashmap:
                count += 1
            res = max(count, res)
        return res        
        