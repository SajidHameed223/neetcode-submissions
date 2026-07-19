class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2: return False
        stack = []
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            else:
                if len(stack) > 0 : last_element = stack.pop() 
                else: return False
                if ch == ")":
                    if last_element != "(":
                        return False
                elif ch == "}":
                    if last_element != "{":
                        return False
                elif ch == "]":
                    if last_element != "[":
                        return False
        if len(stack) == 0: 
            return True
        else: 
            return False