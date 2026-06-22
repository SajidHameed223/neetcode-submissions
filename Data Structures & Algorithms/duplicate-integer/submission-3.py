class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        nums_set = list(nums_set)
        # print(len(nums_set))
        return len(nums_set) != len(nums)