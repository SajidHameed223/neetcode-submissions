class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s += str(len(st)) + "#" + st
        return s

    def decode(self, s: str) -> List[str]:
        array = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            length = int(s[i:j])
            j += 1
            ch = []
            while length > 0:
                ch.append(s[j])
                length -= 1
                j += 1
            array.append("".join(ch)
            )
            i = j
        return array
