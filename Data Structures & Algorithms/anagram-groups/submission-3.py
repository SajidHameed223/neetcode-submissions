class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for ch in strs:
            key = [0] * 26
            for c in ch :
                key[ord(c)-ord('a')] = key[ord(c)-ord('a')]+1
            count = tuple(key)
            result[count].append(ch)
        return list(result.values())                
        