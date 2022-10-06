class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        numCoins = len(coins)
        dp = [float('inf')]*(amount + 1)
        dp[0] = 0
        for i in range(1, numCoins + 1):
            for j in range(coins[i - 1], amount + 1):
                dp[j] = min(dp[j], dp[j - coins[i - 1]] + 1)
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
        