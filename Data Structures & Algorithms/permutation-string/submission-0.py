from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = Counter(s1)
        i = 0
        for j in range(len(s2)):
            if s2[j] in s1:
                counts[s2[j]] -= 1
                while counts[s2[j]] < 0:
                    counts[s2[i]] += 1
                    i += 1
                if j - i + 1 == len(s1):
                    return True
            else:
                i = j + 1
                counts = Counter(s1)


        return False



