class Solution {
    public int numTilings(int n) {
        int[] dp = new int[n + 1];
        int MOD = 1000000007;
        dp[0] = 1;
        dp[1] = 1;
        
        for (int i = 2; i < n + 1; i++){
            long temp = 0;
            temp = (temp + dp[i - 1])%MOD;
            temp = (temp + dp[i -2])%MOD;
            for (int j = 2; j < i; j++){
                temp = (temp + 2 * dp[i - j - 1])%MOD;
            }

            dp[i] = (int) temp%MOD;
        }
        
        return dp[n];
        
    }
}