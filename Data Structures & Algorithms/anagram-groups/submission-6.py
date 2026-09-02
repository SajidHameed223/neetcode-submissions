class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       hashmap = defaultdict(list)
       for ch in strs:
        key = 26 * [0]
        for i in ch:
            key[ord(i) - ord('a')] += 1
        hashmap[tuple(key)].append(ch)
       return list(hashmap.values())
