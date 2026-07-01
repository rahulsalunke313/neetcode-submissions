from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = Counter(t)
        freq = counts.copy()
        vis = set(t)
        i = 0
        j = 0
        ans = ''
        for j in range(len(s)):
            if s[j] in t:
                freq[s[j]] -= 1
                if freq[s[j]] <= 0 and s[j] in vis:
                    vis.remove(s[j])
                if len(vis) == 0:
                    print(s[i:j+1])
                    if not ans:
                        ans = s[i:j+1]
                    elif len(ans) > len(s[i:j+1]):
                        ans = s[i:j+1]
            while i <= j and (s[i] not in t or freq[s[i]] < 0):
                # print(i,j,freq)
                if s[i] in freq:
                    freq[s[i]] += 1
                i += 1
                if len(vis) == 0:
                    if len(ans) > len(s[i:j+1]):
                        ans = s[i:j+1]
                
        return ans













