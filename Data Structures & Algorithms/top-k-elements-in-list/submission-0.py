class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         # k will be the number of element in the result
        # finding the the number that appear the most, top down.
        # [1,2,2,3,3,3], k = 2
        # 1: 1
        # 2: 2          we can use Hashmap sorted the values top down,
        # 3: 3
        
        hashmap = defaultdict(int)

        for i in nums:
            hashmap[i] += 1
        
        i_s = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
        #[(3,3), (2,2), (1,1)]

        print(i_s)

        return list(map(lambda tup: tup[0], i_s[:k]))