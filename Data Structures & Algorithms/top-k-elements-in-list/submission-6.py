class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = []
        for num in  nums:
            hashmap[num] = hashmap.get(num , 0) + 1
        buckets = [[] for i in range(len(nums)+1)]
        print(buckets)
        for key , value in hashmap.items():
            buckets[value].append(key)
        print(buckets)
        for i in range(len(buckets)-1,-1,-1):
            if len(buckets[i]) > 0:
                for num in buckets[i]:
                    result.append(num)
                if len(result) == k:
                    return result
        