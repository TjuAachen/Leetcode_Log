class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1,n+1):
            if i == 1:
                dp[i] = 1
            else:
                for j in range(1,i+1):
                    dp[i] += dp[j-1] * dp[i-j]
        return dp[n]
        