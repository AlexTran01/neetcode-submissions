class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0

        count = {}
        pool = {}
        res = 1

        for n in nums: 
            count[n] = count.get(n, 0) + 1

        while count:
            key, value = count.popitem()
            val = key
            sequenceCount = 1
            
            while True:
                val += 1
                if val in pool:
                    sequenceCount += pool[val]
                    pool.pop(val)
                    break
                elif val in count:
                    count.pop(val)
                    sequenceCount += 1
                else:
                    break
                
            res = max(res, sequenceCount)
            pool[key] = sequenceCount

        return res
            
                    

                    