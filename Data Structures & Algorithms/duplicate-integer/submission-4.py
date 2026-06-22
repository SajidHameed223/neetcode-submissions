class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                return True
            else:
                hash_map[num] = 1
        # nums_set = set(nums)
        # nums_set = list(nums_set)
        # # print(len(nums_set))
        # return len(nums_set) != len(nums)
        return False