class Solution {
    public int coinChange(int[] coins, int amount) {
        int n = coins.length;
        int[][] dp = new int[n + 1][amount + 1];
        dp[0][0] = 0;
        for(int j = 1; j < amount + 1; j++){
            dp[0][j] = -1;
        }
        for(int i = 1; i < n + 1; i ++)
            for(int j = 1; j < amount + 1; j++){
                int curVal = coins[i - 1];
                int left = Integer.MAX_VALUE, right = Integer.MAX_VALUE;
                if( curVal <= j && dp[i][j - curVal] != -1){
                    left = dp[i][j - curVal] + 1 ;
                }
                if(dp[i-1][j] != -1)right = dp[i-1][j];
                dp[i][j] = Math.min(left, right);
                if (dp[i][j] == Integer.MAX_VALUE)dp[i][j] = -1;
            }
        return dp[n][amount];
    }
}