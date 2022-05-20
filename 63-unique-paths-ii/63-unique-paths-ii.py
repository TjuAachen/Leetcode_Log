class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for i in range(m)]
        
        #initial condition
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        
        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] =0
                    continue
                
                if row - 1 >= 0:
                    dp[row][col] += dp[row-1][col]
                if col - 1 >= 0:
                    dp[row][col] += dp[row][col-1]
                    
        return dp[-1][-1]
        

        