class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        hashmap1 = {}
        for i in s:
            hashmap[i] = hashmap.get(i , 0)+1
        for i in t:     
            hashmap1[i] = hashmap1.get(i , 0)+1
        if hashmap == hashmap1:
            return True
        else:
            return False        
        # ss = "".join(sorted(s))
        # st = "".join(sorted(t))
        # if ss == st:
        #     return True
        # else:
        #     return False    