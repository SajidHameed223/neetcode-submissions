class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for s1 in s :
            hashmap[s1] = hashmap.get(s1 , 0) +1
        for t1 in t :
            hashmap[t1] = hashmap.get(t1 , 0) -1
        for h in hashmap:
            if hashmap[h] != 0:
                return False
        return True