class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int nrow = obstacleGrid.length, ncol = obstacleGrid[0].length;
        int[][] dp = new int[nrow][ncol];
        if(obstacleGrid[0][0] == 1)return 0;
        dp[0][0] = 1;
        for(int i = 0; i < nrow; i++)
            for(int j = 0; j < ncol; j++){
                if(obstacleGrid[i][j] == 1){
                    dp[i][j] = 0;
                    continue;
                }
                if(i - 1 >= 0 && obstacleGrid[i-1][j] != 1){
                    dp[i][j] += dp[i-1][j];                
                }
                if( j - 1 >= 0 && obstacleGrid[i][j-1] != 1){
                    dp[i][j] += dp[i][j-1];
                }
            }
        return dp[nrow - 1][ncol - 1];
        
        
    }
}