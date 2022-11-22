class Solution {
    public int numSquares(int n) {
        int[][] dp = new int[n + 1][101];
        
        //initial value
        for(int j = 0; j < n + 1; j++)
            dp[j][0] = Integer.MAX_VALUE;         

        for(int i = 0; i < 101; i++)
            dp[0][i] = 0;        
        
        for(int num = 1; num < n + 1; num++)
            for(int k = 1; k < 101; k++){
                
                dp[num][k] = dp[num][k - 1];
                
                if(num >= k * k)
                    dp[num][k] = Math.min(dp[num - k * k][k] + 1, dp[num][k]);
                
            }
        
        return dp[n][100];
        
    }
}