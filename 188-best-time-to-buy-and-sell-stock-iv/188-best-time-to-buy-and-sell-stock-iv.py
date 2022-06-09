class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        t_cost = [float('inf')] * k
        t_profit = [0] * k
        if k == 0:
            return 0
        for price in prices:
            i = 0
            while(i < k):
                if i == 0:
                    t_cost[i] = min(t_cost[i], price)
                else:
                    t_cost[i] = min(t_cost[i], price - t_profit[i-1])
                t_profit[i] = max(t_profit[i], price - t_cost[i])
                i = i + 1
        return t_profit[-1]