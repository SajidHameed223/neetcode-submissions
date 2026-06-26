class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = float('-inf')
        i , j = 0 , len(heights) - 1
        while i < j: 
            output = 0 
            if heights[i] <= heights[j]:
                output = heights[i] * (j-i) 
                i += 1
            elif heights[i] > heights[j]:
                output = heights[j] * (j-i)
                j -= 1
            result = max(output , result)
        return result