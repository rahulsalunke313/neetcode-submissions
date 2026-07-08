class Solution:
    def findMin(self, nums: List[int]) -> int:
        a = 0
        b = len(nums) - 1
        ans = float('inf')

        while a <= b:
            mid = (a + b) // 2
            print(nums[a],nums[mid],nums[b])
            if nums[a] <= nums[mid]:
                ans = min(nums[a],ans)
                a = mid + 1
            elif nums[mid] <= nums[b]:
                ans = min(ans,nums[mid])
                b = mid - 1
        return ans




                
