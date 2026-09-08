class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_sum = sorted(nums)
        result = []
        for i in range(len(sorted_sum)):
            if i > 0 and sorted_sum[i] == sorted_sum[i - 1]:
                continue
            j, k = i + 1, len(sorted(sorted_sum)) - 1
            while j < k:
                expected_sum = sorted_sum[i] + sorted_sum[j] + sorted_sum[k]
                
                if expected_sum < 0:
                    j += 1
                elif expected_sum > 0:
                    k -= 1
                else:
                    result.append([sorted_sum[i], sorted_sum[j], sorted_sum[k]])
                    j += 1
                    k -= 1
                    while j < k and sorted_sum[j] == sorted_sum[j - 1]:
                        j += 1
                    while j < k and k < (len(sorted_sum) -1) and sorted_sum[k] == sorted_sum[k + 1]:
                        k -= 1
        return result
