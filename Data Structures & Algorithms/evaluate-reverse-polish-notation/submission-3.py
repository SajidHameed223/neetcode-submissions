import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hashmap={
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a , b: int(a/b),
        }
        stack = []
        for token in tokens:
            if token in hashmap:
                b = stack.pop()
                a = stack.pop()
                op = hashmap[token]
                result = op(a,b)
                stack.append(int(result))
            else:
                stack.append(int(token))
        return stack[0]