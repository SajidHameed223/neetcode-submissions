class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left , right = 1 , 1
        n = len(nums)
        res = [1] * n
        for i in range(1 , n):
            left *= nums[i-1]
            res[i] *= left
        for i in range(n-2 , -1 , -1):
            right *= nums[i+1]
            res[i] *= right
        return res          