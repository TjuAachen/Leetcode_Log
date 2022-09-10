class Solution {
    public int maxProfit(int[] prices) {
        int N = prices.length;
        int[][] dp = new int[N][2];
        
        dp[0][1] = -prices[0];
        
        for(int i = 1; i < N; i++){
            int tmp = Math.max(dp[i-1][0] - prices[i], dp[i-1][1]);
            dp[i][1] = tmp;
            
            tmp = Math.max(dp[i-1][1] + prices[i], dp[i-1][0]);
            dp[i][0] = tmp;
        }
        return dp[N-1][0];
        
        
    }
}