class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start , end = 0 , len(numbers) - 1
        while start < end:
            temp = numbers[start] + numbers[end] 
            if (temp == target) and start != end:
                return [start + 1 , end + 1]
            if temp < target :
                start += 1
            else:
                end -= 1
        return []                