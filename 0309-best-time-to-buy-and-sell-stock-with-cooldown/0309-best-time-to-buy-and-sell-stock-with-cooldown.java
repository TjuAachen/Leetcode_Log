class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] dp = new int[n][3];
        //0-buy, 1-cooldown, 2-sell
        dp[0][0] = -prices[0];
        
        for (int cur = 1; cur < n; cur++){
            dp[cur][0] = Integer.MIN_VALUE;
            dp[cur][1] = Integer.MIN_VALUE;
            dp[cur][2] = Integer.MIN_VALUE;
            for (int prev = 0; prev < cur; prev++){
                dp[cur][0] = Math.max(dp[prev][1] - prices[cur], dp[cur][0]);
                dp[cur][1] = Math.max(dp[prev][2], dp[cur][1]);
                dp[cur][2] = Math.max(dp[prev][0] + prices[cur], dp[cur][2]);
            }
        }
        
        return Math.max(Math.max(dp[n - 1][0], dp[n - 1][1]), dp[n -1][2]);
    }
}