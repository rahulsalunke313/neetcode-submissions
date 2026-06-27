class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = 0
        j = 1
        ans = 1
        vis = {s[0]:0}
        while j < len(s):
            if s[j] in vis and vis[s[j]] >= i:
                i = vis[s[j]] + 1
            vis[s[j]] = j
            ans = max(j-i+1,ans)
            j += 1
        return ans

