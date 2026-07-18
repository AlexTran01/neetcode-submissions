class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else: 
                r = mid
        
        # l will point at the min (pivot point):
        print(l)
        # if target == nums[l]: return l

        end_first_ar = l - 1
        begin_second_ar = l
        if end_first_ar == -1:
            l = 0
            r = len(nums) - 1

        elif target >= nums[0] and target <= nums[end_first_ar]:
            l = 0
            r = end_first_ar
        else: 
            r = len(nums) - 1

        print(l, r)

        while l <= r:
            mid = l + (r-l)//2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        
        return -1