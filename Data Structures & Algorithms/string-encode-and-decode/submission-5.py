class Solution:

    def encode(self, strs: List[str]) -> str:
        res =''
        for i in range(len(strs)):
            print(strs[i])
            res+=(str(len(strs[i])))
            res+=("#")
            res+=(strs[i])
        return res
    def decode(self, s: str) -> List[str]:
        print(s)
        result = []
        i = 0 
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
                print(j)
            length = int(s[i:j])
            i = j + 1
            j = length + i
            result.append(s[i:j])
            i = j 
        return result










