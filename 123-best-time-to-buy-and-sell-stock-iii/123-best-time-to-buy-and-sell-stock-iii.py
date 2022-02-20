class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        #[0,left] maximum profit
        left_profit = [0]*length
        #[left, end] maximum profit
        right_profit = [0]*length
        profit = 0
        if length == 1:
            return 0
        
        for ind, price in enumerate(prices):
            if ind == 0:
                min_price = price
            else:
                min_price = min(min_price,price)
            left_profit[ind] = max(profit, price - min_price)
        max_price = 0
        profit = 0
        for ind in range(length-1,-1,-1):
            price = prices[ind]
            max_price = max(max_price,price)
            profit = max(profit, max_price - price)
            right_profit[ind] = profit
        final = 0
        for ind in range(length):
            if ind + 1< length:
                final = max(final,left_profit[ind] + right_profit[ind+1])
            else:
                final = max(final,left_profit[ind])
        return final
            