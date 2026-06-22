class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining not in hashmap :
                hashmap[nums[i]] = i 
            else:
                return [hashmap[remaining] , i ]
        print(hashmap)
        return []