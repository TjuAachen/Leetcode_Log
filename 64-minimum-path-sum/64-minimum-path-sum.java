class Solution {
    public int minPathSum(int[][] grid) {
        int nrow = grid.length, ncol = grid[0].length;
        int[][] dp = new int[nrow][ncol];
        
        for(int i = 0; i < nrow; i++)
            for(int j = 0; j < ncol; j++){
                dp[i][j] = Integer.MAX_VALUE;
                if(i == 0 && j == 0){
                    dp[i][j] = grid[0][0];
                }
                if(i - 1 >= 0){
                    dp[i][j] = Math.min(dp[i-1][j] + grid[i][j], dp[i][j]);
                }
                if(j - 1 >= 0){
                    dp[i][j] = Math.min(dp[i][j - 1] + grid[i][j], dp[i][j]);
                }
            }
        return dp[nrow - 1][ncol - 1];
        
    }
}