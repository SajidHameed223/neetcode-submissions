class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        result = 0
        i = 0 
        j = 0
        while j < len(s):
            if s[j] in hashmap :
                i = max(hashmap[s[j]] + 1 , i)
            hashmap[s[j]] =j
            result = max(result , j -i +1)     
            j+=1 
        return result