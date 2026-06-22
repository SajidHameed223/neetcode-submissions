class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        hashmap1 = {}
        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i] , 0)+1    
            hashmap1[t[i]] = hashmap1.get(t[i] , 0)+1
        return hashmap == hashmap1
     
           
        # ss = "".join(sorted(s))
        # st = "".join(sorted(t))
        # if ss == st:
        #     return True
        # else:
        #     return False    