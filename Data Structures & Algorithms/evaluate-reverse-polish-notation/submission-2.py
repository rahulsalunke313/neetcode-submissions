class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*',  '/'}
        stack = []
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                v2 = stack.pop()
                v1 = stack.pop()
                if t == '+':
                    stack.append(v1 + v2)
                if t == '-':
                    stack.append(v1 - v2)
                if t == '*':
                    stack.append(v1 * v2)
                if t == '/':
                    stack.append(int(v1 / v2))
        return stack.pop()

