class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        buckets = [[] for i in range(len(nums) + 1)]
        for key, value in hashmap.items():
            buckets[value].append(key)
        answer = []
        for i in range(len(buckets)-1,-1,-1):
            if len(buckets[i]) > 0:
                if len(answer) < k:
                    for value in buckets[i]:
                        if len(answer) > k :
                            return answer
                        answer.append(value)
                else:
                    return answer
        return answer
