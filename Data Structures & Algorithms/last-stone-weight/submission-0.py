class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxheap = [-s for s in stones]

        heapq.heapify(maxheap) 
        print(maxheap)

        while len(maxheap) > 1:
            stone1 = heapq.heappop(maxheap)
            # if not maxheap:
            #     return -stone1
            stone2 = heapq.heappop(maxheap)
            print(stone1 ,stone2)
            if stone1 == stone2:
                pass
            
            heapq.heappush(maxheap, stone1-stone2)
            # print(ma)
            
        if maxheap:
            return -maxheap[0]
        else:
            return 0