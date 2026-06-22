class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap = {}
        # for 
        ss = "".join(sorted(s))
        st = "".join(sorted(t))
        if ss == st:
            return True
        else:
            return False    