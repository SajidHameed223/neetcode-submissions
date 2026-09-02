class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if nums[i] not in hashmap:
                hashmap[remaining] = i 
            else:
                return [hashmap[nums[i]], i]