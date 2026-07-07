class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1) ] #empty list to hold number for each number of frequency

        for num in nums:    
            count[num] = 1 + count.get(num, 0)

        for n, c in count.items():
            freq[c].append(n)
        # each freq column, there is a list that contains all numbers

        res = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if(len(res) == k):
                    return res
        