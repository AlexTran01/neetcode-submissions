class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
         
        if total % 2 != 0:
            return False
        
        half = total // 2
       
        memo = {}

        def dp(total, i):
            if (total, i) in memo:
                return memo[(total, i)]

            if total == half:
                return True
            
            if i == n or total > half:
                return False


            res = dp(total, i+1)
            if not res and total+nums[i] <= half:
                res = dp(total+nums[i], i+1)
            
            memo[(total, i)] = res
            return res

        return dp(0, 0)

        
