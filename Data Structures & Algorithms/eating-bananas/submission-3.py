
class Solution:

    def checkK(self, k: int, piles: List[int], h:int) -> bool:
        if k == 0: return False
        count = 0
        for i in range(len(piles)):
            count += math.ceil(piles[i] / k)
            if count > h:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_banas = max(piles)

        avg_hour_per_pile = h // len(piles)

        max_k = math.ceil(max_banas / avg_hour_per_pile) # double negation -> ceil up.
        min_k = max_k

        print(f"max_bans: {max_banas}, avg_hour: {avg_hour_per_pile}, max_k: {max_k}")

        
        while self.checkK(k= math.ceil(min_k / 2), piles=piles, h=h):
            if min_k == 1:
                break
            min_k = math.ceil(min_k / 2)
            print(min_k)

        ## moving slowly
        while self.checkK(k=min_k - 1, piles=piles, h=h):
            min_k = min_k - 1
            # print(min_k)
        return min_k


