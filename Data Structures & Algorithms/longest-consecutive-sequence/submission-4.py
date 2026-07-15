class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        result = 0 
        for num in hashmap:
            if num - 1 not in hashmap:
                count = 1 
                number = num
                while number + 1 in hashmap:
                    count += 1
                    number += 1
                result = max(result , count)
        return result



