class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # dynamic programming
        #dp[i][j] to reach [i, j] the minimum health
        nrow, ncol = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * ncol for _ in range(nrow)]
        for i in range(nrow-1, -1, -1):
            for j in range(ncol-1, -1, -1):
                down, right = float('inf'), float('inf')
                if i < nrow - 1:
                    right =  dp[i+1][j]
                if j < ncol - 1:
                    down = dp[i][j+1]
                if dungeon[i][j] >= 0:
                    dp[i][j] = max(min(right, down) - dungeon[i][j], 1)
                else:
                    dp[i][j] = max(min(down, right) - dungeon[i][j], 1)
                if i == nrow - 1 and j == ncol - 1:
                    if dungeon[i][j] >= 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 - dungeon[i][j]
        print(dp)
        return dp[0][0]
        
        
        
        