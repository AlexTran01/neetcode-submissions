class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r-l) // 2
           
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
    
        def bns (arr, target):
            if arr is None: 
                return -1

            l, r = 0, len(arr)-1
            while l <= r:

                mid = l + (r-l) // 2

                if arr[mid] == target:
                    return mid
                if target > arr[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
                

            return -1

        if target == nums[len(nums) - 1]:
            return len(nums)-1
        elif target < nums[len(nums) - 1]:
            print(f"target is in upper part, {nums[r:]}, ")
            val = bns(nums[r:], target)
            return r + val if val != -1 else val
        else:
            print("target is in lower part")
            return bns(nums[:r], target)

        
    

