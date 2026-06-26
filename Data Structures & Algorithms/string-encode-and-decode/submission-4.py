class Solution:

    def encode(self, strs: List[str]) -> str:
        s = '€'.join(strs) 
        print('en--',s, len(strs))
        return s + '€' +str(len(strs))

    def decode(self, s: str) -> List[str]:
        if int(s[-1]) == 0:
            return []
        print('de--',s)
        s = s.split('€')[:-1] 
        return s
