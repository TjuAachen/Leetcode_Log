class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0] * (k + 1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            dp[i][0] = 1
        dp[0][0] = 1
        for i in range(1,n+1):
            for j in range(1, k+1):
                    if j <= i - 1:
                        dp[i][j] += dp[i][j-1] + dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-1]-dp[i-1][j-i] + dp[i-1][j]
                       
                        
      #  print(dp)
        return dp[-1][-1] % (10**9 + 7)