class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        #0-相同,1-不同
        dp = [[0 for _ in range(2)] for _ in range(n+1)]
        dp[1][0] = 0
        dp[1][1] = k
        if n > 1:
            dp[2][0] = k
            dp[2][1] = k*(k-1)
        
        for i in range(3,n+1):
            dp[i][0] = dp[i-1][1]
            dp[i][1] = dp[i-1][0] * (k -1) + dp[i-1][1] * (k -1)
        return sum(dp[-1])%(2**31)
        
        
        
        