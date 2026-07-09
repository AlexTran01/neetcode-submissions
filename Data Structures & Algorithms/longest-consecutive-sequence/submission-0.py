class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # min
        lastNum = min(nums)
        # create hastable: to see if we has alreadu check for a number
        table = set()
        count = 1
        n = len(nums)
        table.add(lastNum)

        while True:
            temp = count

            for i in range(n):
                if(count == n):
                    return n
                
                if(nums[i] in table):
                    continue
                
                if(nums[i] - lastNum == 1):
                    lastNum = nums[i]
                    table.add(nums[i])
                    count += 1

            if temp == count:
                return count