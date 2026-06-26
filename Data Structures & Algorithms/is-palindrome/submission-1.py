class Solution:
    def isPalindrome(self, s: str) -> bool:

        # s = ''.join([''.join([v for v in k if v.isalnum()]) for k in s.split(' ')]).lower()
        a = ''.join([char for char in s.lower() if char.isalnum()])
        return a == a[::-1]