class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pool = set(nums)
        longest = 0
        
        for e in pool:
            if (e - 1) not in pool:
                # e is starting pos:
                length = 1
                while (e + length) in pool:
                    length += 1
                longest = max(length, longest)
                    
        return longest
                    

                    