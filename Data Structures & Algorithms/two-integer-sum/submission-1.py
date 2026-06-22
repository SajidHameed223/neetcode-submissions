class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       count = {}
       for i in range(len(nums)):
        temp = target - nums[i]
        if nums[i] not in count:
            count[temp] = i 
        else:
            return [count[nums[i]] , i ]

               
