class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k = 0

        # # 2323 , val = 3
        # n = len(nums)
        # i = 0
        # lastNoneVal = 0 # 1

        # while i < n: # 1

        #     if nums[i] == val: # nums[i] = 3

        #         lastNoneVal = max(lastNoneVal, i)

        #         while lastNoneVal < n and nums[lastNoneVal] == val:
        #             lastNoneVal += 1
                
        #         if lastNoneVal == n:
        #             return k
        #         # print(lastNoneVal)
        #         nums[i], nums[lastNoneVal] = nums[lastNoneVal], nums[i]
        #         # print(nums[i], nums[lastNoneVal])
                
        #     if nums[i] != val:
        #         k += 1
        
        #     i += 1

        # return k
        ans= []
        for i in range(len(nums)):
            if nums[i] != val:
                ans.append(nums[i])
        for i in range(len(ans)):
            nums[i] = ans[i]

        return len(ans)
                