class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            key = 26 * [0]
            for ch in s:
                key[ord(ch) - ord("a")] += 1
            result[tuple(key)].append(s)
        return [value for value in result.values()]
