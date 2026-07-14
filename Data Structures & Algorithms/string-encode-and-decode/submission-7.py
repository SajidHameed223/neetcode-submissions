class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for st in strs:
            s += str(len(st)) + '#' + st
        return s
    def decode(self, s: str) -> List[str]:
        i = 0 
        strs = []
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j = j + 1
            count = int(s[i:j])
            ch = ""
            j += 1
            while count > 0:
                ch += s[j]
                j += 1
                count -= 1
            strs.append(ch)
            i = j 
            j += 1
        return strs
