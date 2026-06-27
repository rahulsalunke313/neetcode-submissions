class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0 
        j = len(heights) -1
        cur = 0
        ans = 0
        while i < j:
            cur = (j-i)*min(heights[i],heights[j])
            ans = max(cur,ans)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            print(heights[i],heights[j])
        return ans

