class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ans = []
        # for i in range(len(temperatures)-1):
        #     f = False
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             f = True
        #             ans.append(j-i)
        #             break
        #     if not f:
        #         ans.append(0)
        # ans.append(0)
        # return ans
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                waiting_index = stack.pop()
                result[waiting_index] = i - waiting_index
            stack.append(i)
        return result

