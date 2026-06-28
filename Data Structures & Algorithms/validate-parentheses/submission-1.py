class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '{': '}',
            '[':']',
            '(':')',
        }
        stack = []
        for c in s:
            if c in pairs:
                stack.append(c)
            elif not stack:
                return False
            else:
                cp = stack.pop()
                if pairs[cp]  != c:
                    return False
        return len(stack) == 0

