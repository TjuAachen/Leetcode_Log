class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[True]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i >= j:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
        record = {}
        res = [0] * n
        for i in range(1,n):
            if dp[0][i]:
                res[i] = 0
                continue
            ans = float('inf')
            for j in range(1, i+1):
                if dp[j][i]:
                    ans = min(ans, res[j-1] + 1)
            res[i] = ans
        return res[n-1]

        