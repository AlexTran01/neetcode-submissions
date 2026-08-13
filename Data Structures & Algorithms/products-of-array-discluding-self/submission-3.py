class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        res = [0] * len(nums)

        prev = 1
        for i in range(len(nums)):
            prefix[i] = prev
            prev = nums[i] * prev
        
        post = 1
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = post
            post = nums[i] * post
        
        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]
        return res
        