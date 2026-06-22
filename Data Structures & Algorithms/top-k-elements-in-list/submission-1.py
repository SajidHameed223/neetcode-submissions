class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo = {}
        for num in nums:
            memo[num] = memo.get(num , 0 ) + 1
        arr = []        
        for key , val in memo.items():
            arr.append([val , key])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res    
           