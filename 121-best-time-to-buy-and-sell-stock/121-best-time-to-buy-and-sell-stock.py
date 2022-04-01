class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        stack = []
        res = 0
        for price in prices:
            if not stack:
                stack.append(price)
            while(stack and stack[-1] > price):
                stack.pop()
            stack.append(price)
            res = max(res, stack[-1] - stack[0])
        return res
        