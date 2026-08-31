class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        for ch in s:
            hashmap_s[ch] = hashmap_s.get(ch, 0) + 1
        for ch in t:
            hashmap_s[ch] = hashmap_s.get(ch, 0) - 1
        for ch in hashmap_s:
            if hashmap_s[ch] != 0: return False
        return True
