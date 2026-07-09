class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + ((r - l) // 2)

            if mid == l or mid == r:
                return -1
            
            if target == nums[mid]:
                return mid
            
            if target < nums[mid]:
                r = mid 
            else:
                l = mid

        return res