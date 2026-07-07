class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pool = set(nums)
        count = 0
        for e in pool:
            if (e - 1) not in pool:
                # e is starting pos:
                temp = e
                tempCount = 1
                while True:
                    if (temp+1) in pool:
                        tempCount += 1
                        temp += 1
                    else:
                        if tempCount > count:
                            count = tempCount
                        break
        return count
                    