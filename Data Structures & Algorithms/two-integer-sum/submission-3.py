class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if nums[i] not in hashmap:
                hashmap[remaining] = i 
            else:
                return [hashmap[nums[i]] , i]
            print(hashmap)
        return []

        # for i in range(len(nums)):
        #     for j in range(i+1 , len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i , j]
        # TC = O( N ^ 2 )
        # SC = O( 1 )