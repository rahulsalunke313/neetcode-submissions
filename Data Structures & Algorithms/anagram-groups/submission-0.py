class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagrams(s: str, t: str):
            return sorted(s) == sorted(t)
        pairs = {}
        for s in strs:
            found = False
            for k in pairs:
                if isAnagrams(s, k):
                    pairs[k].append(s)
                    found = True
                    continue
            if not found:
                pairs[s] = [s]
        return [[v for v in pairs[k]] for k in pairs]
            
            
