class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        len_s = dict()
        for ch in s:
            len_s[ch] = len_s.get(ch,0)+1
        for ch in t:
            len_s[ch] = len_s.get(ch,0)-1
        for ch in len_s.values():
            if ch != 0:
                return False
        return True