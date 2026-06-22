class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for c in s :
            hashmap[c] = hashmap.get(c , 0) + 1 
        for c in t:
            hashmap[c] = hashmap.get(c , 0) - 1 
        for num in hashmap:
            if hashmap[num] != 0:
                return False
        return True                