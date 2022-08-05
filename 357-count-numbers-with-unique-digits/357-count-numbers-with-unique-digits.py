class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
  #      count = 1
        for i in range(1, n + 1):
            #non-leading 0
            count = 9
            for j in range(1,i):
                count *= (10 - j)
            dp[i] += count
            
            dp[i] += dp[i-1]
        return dp[n]