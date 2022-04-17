class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i == j:
                    dp[i][j] = 1
                if i!= j and s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                elif i != j:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][-1]