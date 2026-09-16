class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        n1 = len(s1)
        hashmap = Counter(s1)
        hashmap1 = {}
        l = 0
        for r in range(len(s2)):
            while r-l+1 > n1:
                hashmap1[s2[l]] -=1
                if hashmap1[s2[l]] == 0: hashmap1.pop(s2[l])
                l += 1
            hashmap1[s2[r]] = hashmap1.get(s2[r], 0) + 1
            if hashmap1 == hashmap:
                return True
        return False
