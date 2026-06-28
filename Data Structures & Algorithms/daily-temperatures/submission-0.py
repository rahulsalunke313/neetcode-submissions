class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        for i in range(len(temperatures)-1):
            f = False
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    f = True
                    ans.append(j-i)
                    break
            if not f:
                ans.append(0)
        ans.append(0)
        return ans
