class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i , j = 0 , len(numbers) - 1 
        while i < j:
            number = numbers[i] + numbers[j]
            if number == target:
                return[i + 1 , j + 1]
            elif number < target:
                i += 1
            else:
                j -= 1
        
