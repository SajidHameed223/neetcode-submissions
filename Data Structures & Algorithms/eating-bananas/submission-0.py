class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start , end = 1 , max(piles)
        while start <= end :
            mid = start + (end - start) // 2 
            k = 0 
            for i in range(len(piles)):
                k += (piles[i] + mid - 1) // mid 
            if k > h:
                start = mid +1 
            else:
                end = mid -1 
        return start                                 