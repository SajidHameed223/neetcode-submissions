class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num , 0 ) + 1 
        heap = []
        for key,val in count.items():
            if len(heap) < k or val > heap[0][0]:
                heapq.heappush(heap , (val , key))
            if len(heap) > k :
                heapq.heappop(heap)
        return [i[1] for i in heap]            
                   