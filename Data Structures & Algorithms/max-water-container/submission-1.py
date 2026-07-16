class Solution:
    def maxArea(self, nums: List[int]) -> int:
        i , j = 0 , len(nums) - 1
        result = 0 
        while i < j:
            area = 0
            if nums[i] < nums[j]:
                area = nums[i] * (j-i)
                i += 1
            else:
                area = nums[j] * (j-i)
                j -= 1
            result = max(result , area)
        return result