class Solution {
    public int maxProfit(int k, int[] prices) {
        int N = prices.length;
        int[][] dp = new int[N][k+1];
        if(k == 0)return 0;
        int ans = 0;
        for(int i = 1; i < N; i++)
            for(int j = k-1; j >= 0; j--){
                dp[i][j] = Math.max(dp[i][j], dp[i-1][j]);
                for(int t = 0; t <= i; t++){
                dp[i][j] = Math.max(dp[i][j], dp[i-t][j+1] +prices[i] -prices[i-t]);
                    }
                if(i == N -1){
                    ans = Math.max(dp[i][j], ans);
                }
                
            }
        return ans;
        
    }
}