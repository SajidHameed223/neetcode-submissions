class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
         ")":"(",
         "}":"{",
         "]":"["
        }
        stack = []
        for ch in s:
            if ch in hashmap:
                if stack and stack[-1] != hashmap[ch]:
                    return False
                else:
                    if stack:
                        stack.pop()
                    else: 
                        return False
            else:
                stack.append(ch)
        return True if len(stack) == 0 else False