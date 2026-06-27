class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = set()
        result = 0
        i = 0 
        j = 0
        while j < len(s):
            while s[j] in hashmap :
                hashmap.remove(s[i])
                i += 1
            hashmap.add(s[j])
            result = max(result , j - i + 1)      
            j+=1      
        return result