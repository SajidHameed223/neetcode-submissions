class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = []
        for num in nums:
            hashmap[num] = hashmap.get(num ,0) + 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for key , value in hashmap.items():
            bucket[value].append(key)
        for i in range(len(bucket) -1 , -1 , -1):
            if len(result) == k:
                return result 
            else:
                if len(bucket[i]) > 0 :
                    for b in bucket[i]:
                        if len(result) == k:
                            return result 
                        result.append(b)
        return result



            