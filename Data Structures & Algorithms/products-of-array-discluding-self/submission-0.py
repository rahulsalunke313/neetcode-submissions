class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [nums[0]]
        for i in nums[1:]:
            pre.append(pre[-1] * i)
        post = [nums[-1]]
        for i in nums[len(nums)-2::-1]:
            post.append(post[-1] * i)
        post = post[::-1]
        ans = [post[1]]
        for i in range(1, len(nums)-1):
            ans.append(pre[i-1] * post[i+1])
        ans.append(pre[-2])
        return ans
