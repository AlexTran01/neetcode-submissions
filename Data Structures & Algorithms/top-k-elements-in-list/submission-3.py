class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        order = []
        res = []

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for key, value in count.items():
            order.append((value, key))
        
        order = sorted(order ,key = lambda x: x[0], reverse = True)

        for i in range(k):
            res.append(order[i][1])
        
        return res