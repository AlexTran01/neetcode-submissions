class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cumulProduct = [1 for i in range(len(nums))]
        res = [1 for i in range(len(nums))]
        cumulProduct[0] = nums[0] 

        i = 1
        while i <len(nums): # O(n)
            res[0] *= nums[i]
            cumulProduct[i] = nums[0] * res[0]
            i += 1

        i = 1
        while i < len(nums): # O(n)
            j = i+1
            remainProduct = 1
            while j < len(nums): 
                remainProduct *= nums[j] 
                j += 1
            res[i] = cumulProduct[i-1] * remainProduct
            i += 1

        return res