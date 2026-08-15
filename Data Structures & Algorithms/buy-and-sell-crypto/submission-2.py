class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None:
            return 0

        buyPrice = float("inf")
        maxProf = 0

        for p in prices:
            if p < buyPrice:
                buyPrice = p
            else:
                maxProf = max(maxProf, p - buyPrice)
                
        return maxProf