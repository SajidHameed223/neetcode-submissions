class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        store_water = 0
        while i < j:
            length = 0
            width = j - i
            if heights[i] < heights[j]:
                length = heights[i]
                i += 1
            elif heights[i] >= heights[j]:
                length = heights[j]
                j -= 1
            area = length * width
            store_water = max(store_water, area)
        return store_water
