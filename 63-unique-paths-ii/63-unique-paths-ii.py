class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for i in range(m)]
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        for i in range(m-1,-1,-1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j] != 1 and i < m-1 and j < n-1:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
                elif obstacleGrid[i][j] != 1 and i == m-1 and j < n - 1:
                    dp[i][j] = dp[i][j+1]
                elif obstacleGrid[i][j] != 1 and j == n-1 and i < m-1:
                    dp[i][j] = dp[i+1][j]
                elif i == m - 1 and j == n-1:
                    dp[i][j] = 1
        return dp[0][0]
        