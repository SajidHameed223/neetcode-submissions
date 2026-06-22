class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for ch in strs:
            length = len(ch)
            s += str(length)+ '#' + ch
        return s
    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0 
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1 
            j = i + length
            arr.append(s[i:j])  
            i = j  
        return arr    