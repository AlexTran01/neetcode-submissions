class Solution:
     def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):

            if a > 0: 
                break

            if a == nums[i-1] and i > 0:
                continue

            findingTarget = -nums[i]
            # two sum:
            r, l = len(nums)-1 , i + 1
            while(l < r):
                if (s := nums[r] + nums[l] == findingTarget):
                    res.append([a, nums[r], nums[l]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif s > findingTarget:
                    r -= 1
                else:
                    l += 1
        return res