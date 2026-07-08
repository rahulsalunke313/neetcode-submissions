class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums)- 1

        while a <= b:
            m = (a+b) //2 
            if nums[m] == target:
                return m
            if nums[m] > nums[b]:
                if nums[a] <= target and target < nums[m]:
                    b = m - 1
                else:
                    a = m + 1
            else:
                if target <= nums[b] and nums[m] < target:
                    a = m + 1
                else:
                    b = m - 1
        return -1
                
