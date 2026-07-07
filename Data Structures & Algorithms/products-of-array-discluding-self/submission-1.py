class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rtl = [1 for i in range(len(nums))]
        ltr = [1 for i in range(len(nums))]
        res = [1 for i in range(len(nums))]
        n = len(nums)
        rtl[0] = nums[0]
        ltr[n-1] = nums[n-1]

        i = 1 
        while i < n: #O(n)
            rtl[i] = rtl[i-1] * nums[i]
            i += 1

        i = n-2
        while i >= 0: #O(n)
            ltr[i] = ltr[i+1] * nums[i]
            i -= 1
        
        i = 0
        while i < n: #O(n)
            if i == 0:
                res[i] = ltr[i+1]

            elif i == n-1:
                res[i] = rtl[i-1]

            else:
                res[i] = rtl[i-1] * ltr[i+1]

            i += 1

        return res