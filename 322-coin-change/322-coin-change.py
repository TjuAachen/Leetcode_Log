class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for i in range(len(coins)):
            for j in range(coins[i],amount+1):
                dp[j]=min(dp[j-coins[i]]+1,dp[j])
        if dp[amount]==amount+1:
            dp[amount]=-1
        return dp[amount]
        