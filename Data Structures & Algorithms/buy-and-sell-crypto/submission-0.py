class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_min_i = 0
        cur_i = 0
        max_profit = 0
        while cur_i < len(prices):
            if prices[left_min_i] > prices[cur_i]:
                left_min_i = cur_i
            else:
                max_profit = max(max_profit, (prices[cur_i] - prices[left_min_i]))
            # print(cur_i, left_min_i)
            cur_i += 1
        return max_profit