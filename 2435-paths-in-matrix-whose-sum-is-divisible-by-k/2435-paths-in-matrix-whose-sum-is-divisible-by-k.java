class Solution {
    public int numberOfPaths(int[][] grid, int k) {
        int nrow = grid.length;
        int ncol = grid[0].length;
        int MOD = 1000000000 + 7;
        int[][][] dp = new int[nrow][ncol][k];
        for(int row = 0; row < nrow; row++)
            for(int col = 0; col < ncol; col++)
                for(int num = 0; num < k; num++){
                    int remaining = Math.floorMod(num - grid[row][col], k);
                    if (row == 0 && col == 0)
                        dp[row][col][grid[0][0] % k] = 1;
                    if (row > 0)
                        dp[row][col][num] =(dp[row][col][num] + dp[row - 1][col][remaining] )%MOD;
                    
                    if (col > 0)
                        dp[row][col][num] = (dp[row][col][num] + dp[row][col - 1][remaining] ) %MOD;
                    }
        return dp[nrow - 1][ncol - 1][0];
    }
}