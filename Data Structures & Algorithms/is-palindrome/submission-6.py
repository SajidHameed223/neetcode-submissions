class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for ch in s:
            if ch.isalnum():
                string += ch.lower()
        reverse = ""
        for i in range(len(string) - 1 ,-1 ,-1):
            reverse += string[i]
        
        return string == reverse