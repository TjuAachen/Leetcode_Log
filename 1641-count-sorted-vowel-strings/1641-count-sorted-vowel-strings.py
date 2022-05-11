class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        vowels = ['a','e','i','o','u']
        dp = [[0]*5 for _ in range(n+1)]
        for i in range(5):
            dp[1][i] = 1
        for row in range(1,n+1):
            for col in range(5):
                for k in range(col+1):
                    dp[row][col] += dp[row-1][k]
        return sum(dp[n][:])
        