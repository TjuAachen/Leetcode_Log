class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        N = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[[0] * k for i in range(n+1)] for j in range(m+1)]
        dp[1][1][grid[0][0] % k] = 1
        for i in range(m):
            for j in range(n):
                for t in range(k):
                    dp[i+1][j+1][(t + grid[i][j]) % k] += (dp[i+1][j][t] + dp[i][j+1][t]) % N
        return dp[m][n][0]
                        
                        
                        