class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pool = set()
        for num in nums:
            if num in pool:
                return True
            else:
                pool.add(num)



        return False