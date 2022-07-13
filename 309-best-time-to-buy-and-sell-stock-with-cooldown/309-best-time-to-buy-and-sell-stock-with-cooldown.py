class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        diff = [prices[i] - prices[i-1] for i in range(n) if i > 0]

        if n == 1:
            return 0
        if n == 2:
            return max(0, diff[0])
      #  diff.append(-1)
        ans = 0
        dp = [[0] * 4 for _ in range(n-1)]
        #0-3 : 0: 00 1:01 2:10 3:11
        res = 0
        for i in range(4):
            if i % 2 != 0:
                dp[0][i] = diff[0]
                dp[1][i] = max(dp[0]) + diff[1]
            else:
                dp[1][i] = max(dp[0])
            res = max(res, dp[1][i])
            res = max(res, dp[0][i])
            
        for i in range(2, n-1):
            dp[i][0] = max(dp[i-1][0],dp[i-1][2])
            dp[i][1] = max(dp[i-1][0],dp[i-1][1]) + diff[i]
            dp[i][2] = max(dp[i-1][1],dp[i-1][3]) 
            dp[i][3] = dp[i-1][1] + diff[i]
            res = max(dp[i])
        return res
        