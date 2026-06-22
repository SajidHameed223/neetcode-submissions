class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 
        seq = 0
        for num in nums:
            if num - 1  not in hashmap:
                cur = 1
                while num + cur in hashmap:
                    cur += 1    
                seq = max(seq , cur)
        return seq