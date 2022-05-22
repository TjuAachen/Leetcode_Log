class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        
        for i in range(n-1,-1,-1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j] and i+1 <= j - 1:
                    dp[i][j] = dp[i+1][j-1]
                elif s[i] == s[j] and i + 1 == j:
                    dp[i][j] = True
        count = 0
        for i in range(n):
            for j in range(i,n):
                if dp[i][j] == True:
                    count += 1
        return count
        