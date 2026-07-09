class Solution:

    def checkK(self, k: int, piles: List[int], h:int, return_count:List[int] = [0]) -> bool: 
        if k == 0: return False
        count = 0 # count > h : too low, count < h: too high
        for i in range(len(piles)):
            count += math.ceil(piles[i] / k)
        
        return_count[0] = count

        return count <= h

    def minEatingSpeed(self, piles: List[int], h :int) ->int:
        max_banas = max(piles)
        avg_hour_per_pile = h // len(piles)
        max_k = math.ceil(max_banas / avg_hour_per_pile) # double negation -> ceil up.
        
        l = 1
        r = max_k
        mid = 1
        return_count = [0]

        while l <= r:
            mid = l + ((r - l) // 2)

            if self.checkK(k=mid, piles=piles, h=h, return_count=return_count) and (not self.checkK(k=mid-1, piles=piles, h=h)):
                return mid
    
            if return_count[0] < h: # count is too big
                r = mid - 1
            else:                   # count is too small
                l = mid + 1

        return mid

