class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        res = 0
        i = 0
        for j in range(len(s)):
            while s[j] in hashmap:
                hashmap.pop(s[i])
                i += 1
            hashmap[s[j]] = 1
            res = max(res, j - i + 1)
        return res
