class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0]
        cur_left_max = 0
        right_max = [0]
        cur_right_max = 0
        for i in range(len(height)-1,0,-1):
            cur_right_max = max(cur_right_max, height[i])
            right_max.append(cur_right_max)
        for i in range(1,len(height)):
            cur_left_max = max(cur_left_max, height[i-1])
            left_max.append(cur_left_max)
        right_max = right_max[::-1]
        ans = 0
        for i in range(len(height)):
            ans += max(min(right_max[i],left_max[i]) - height[i],0)

        return ans

