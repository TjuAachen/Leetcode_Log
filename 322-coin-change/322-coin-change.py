class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        numCoins = len(coins)
        dp = [[float('inf')]*(amount + 1) for _ in range(numCoins + 1)]
        dp[0][0] = 0
        for i in range(1, numCoins + 1):
            for j in range(amount + 1):
                if j == 0:
                    dp[i][j] = 0
                    continue
                if coins[i - 1] <= j:
                    dp[i][j] = min(dp[i][j], dp[i][j - coins[i - 1]] + 1)
                dp[i][j] = min(dp[i][j], dp[i-1][j])
        if dp[numCoins][amount] == float('inf'):
            return -1
        return dp[numCoins][amount]
        