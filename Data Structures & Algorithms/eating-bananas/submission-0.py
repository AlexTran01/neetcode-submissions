class Solution:

    def checkK(self, k: int, piles: List[int], h:int) -> bool:
        count = 0
        for i in range(len(piles)):
            count += - ( - piles[i] // k)
            if count > h:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_banas = max(piles)
        avg_hour_per_pile = h // len(piles)

        max_k = - (-max_banas // avg_hour_per_pile) # double negation -> ceil up.
        min_k = max_k

        while self.checkK(k=min_k - 1, piles=piles, h=h):
            min_k = min_k - 1
        
        return min_k
