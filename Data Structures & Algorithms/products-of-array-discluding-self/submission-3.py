class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_product = [1] * n
        post_product = [1] * n
        result = [1] * n
        for i in range(1, n):
            pre_product[i] = pre_product[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            post_product[i] = post_product[i + 1] * nums[i + 1]
        for i in range(n):
            result[i] = post_product[i] * pre_product[i]
        return result
        
