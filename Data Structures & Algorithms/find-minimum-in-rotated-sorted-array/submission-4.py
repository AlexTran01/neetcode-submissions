
class Solution:
    def findMin1(self, nums: List[int]) -> int:
        if nums[0] < nums[len(nums) - 1]:
            return nums[0]
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + int((r - l) / 2)
            if nums[mid] >= nums[r] and nums[mid] >= nums[l]:
                l = mid + 1

            elif nums[mid] <= nums[r] and nums[mid] <= nums[l]: 
                r = mid
            
            elif nums[mid] < nums[r] and nums[mid] > nums[l]:
                r = mid - 1
        return nums[r]
    
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            mid = l + (r-l)//2
            if nums[mid] < nums[r]:
                r = mid
            else: 
                l = mid + 1
        
        return nums[l]