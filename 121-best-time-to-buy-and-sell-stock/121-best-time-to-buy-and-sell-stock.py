class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, max_price = 0, 0
        for i in range(len(prices)-1, -1, -1):
            max_price = max(prices[i],max_price)
            profit = max(profit, max_price-prices[i])
        return profit