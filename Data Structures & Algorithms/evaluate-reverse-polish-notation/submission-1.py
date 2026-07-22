import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hashmap = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": lambda a, b: int(a / b),  # truncates toward zero as LeetCode requires
}
        stack = []
        for token in tokens:
            if token not in hashmap:
                stack.append(int(token))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                op = hashmap[token]
                result = op(val2, val1)
                stack.append(result)
        print(stack)
        return stack[-1]