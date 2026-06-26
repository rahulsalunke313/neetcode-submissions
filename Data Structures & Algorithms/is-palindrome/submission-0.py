class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join([''.join([v for v in k if v.isalnum()]) for k in s.split(' ')]).lower()
        print(s[::-1])
        return s == s[::-1]